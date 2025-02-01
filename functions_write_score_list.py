from moviepy import VideoFileClip, TextClip, CompositeVideoClip

def read_who_scores_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            whoscore = []
            for line in file:
                # Remove leading/trailing whitespace and convert to uppercase
                line = line.strip().upper()
                if 'HOME' or 'AWAY':
                    whoscore.append(line)
            return whoscore
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

DEFAULT_TEXT_FONT = 'C:/Windows/Fonts/Arial.ttf'
DEFAULT_TEXT_SIZE = 150
DEFAULT_TEXT_COLOR = 'white'
DEFAULT_HORIZONTAL_POSITION = "center"

def create_text(text, vertical_position, start_time, end_time):
    kwargs = {
        'text': text,
        'font': DEFAULT_TEXT_FONT,
        'font_size': DEFAULT_TEXT_SIZE,
        'color': DEFAULT_TEXT_COLOR
    }

    txt_clip = TextClip(**kwargs)
    txt_clip = txt_clip.with_position((DEFAULT_HORIZONTAL_POSITION, vertical_position)).with_start(start_time).with_duration(end_time-start_time)
    return txt_clip

time_to_seconds = lambda s: sum(int(x) * 60 ** i for i, x in enumerate(reversed(s.split(":"))))

def add_text_to_video(input_video_name, postfix_scorename, times, who_scores):

    # get the text from score
    text_score = []
    home = 0
    away = 0
    for index, who_score in enumerate(who_scores):
        if who_score.upper() == 'HOME':
            home += 1
        elif who_score.upper() == 'AWAY':
            away += 1
        text_score.append(f"{home} - {away}") 

    # update text format to second format
    times_in_seconds_format = []
    for index, time in enumerate(times):
        times_in_seconds_format.append(time_to_seconds(time))
            
    for index, time in enumerate(times_in_seconds_format):

        # Load the video
        video = VideoFileClip(f"{input_video_name}_{index+1}.mp4")
        video_list = []
        video_list.append(video)

        # Get the video dimensions
        width, height = video.size
        vertical_position = height*0.8

        if index == 0:
            video_list.append(create_text("0 - 0", vertical_position, 0, 7))
        else:
            video_list.append(create_text(text_score[index-1], vertical_position, 0, 7))
        video_list.append(create_text(text_score[index], vertical_position, 7, 11))
        
        # Composite video
        video = CompositeVideoClip(video_list)

        # Output the video
        output_video = f"{input_video_name}_{index+1}_{postfix_scorename}.mp4"
        video.write_videofile(output_video, codec="libx264")

    return None
