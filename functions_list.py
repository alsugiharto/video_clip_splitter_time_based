import re
from datetime import datetime, timedelta
import subprocess

def read_times_from_file(file_path):
    """
    Reads a list of times from a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of times in the format 'HH:MM:SS'.
    """
    try:
        with open(file_path, 'r') as file:
            times = []
            for line in file:
                # Remove leading/trailing whitespace and convert to uppercase
                line = line.strip().upper()
                # Use regular expression to match time in 'HH:MM:SS' format
                match = re.search(r'\b(\d{2}:\d{2}:\d{2})\b', line)
                if match:
                    times.append(match.group(1))
            return times
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
        
def add_seconds(time_str, seconds):
    """
    Add seconds to a given time string.

    Args:
        time_str (str): Time string in the format 'HH:MM:SS'.
        seconds (int): Number of seconds to add.

    Returns:
        str: Time string with the added seconds.
    """
    time = datetime.strptime(time_str, '%H:%M:%S')
    new_time = time + timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')

def subtract_seconds(time_str, seconds):
    """
    Subtract seconds from a given time string.

    Args:
        time_str (str): Time string in the format 'HH:MM:SS'.
        seconds (int): Number of seconds to subtract.

    Returns:
        str: Time string with the subtracted seconds.
    """
    time = datetime.strptime(time_str, '%H:%M:%S')
    new_time = time - timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')

def makes_ffmpeg_script_from_times_between(file_name, result_file_name, times_list):
    """
    makes list of ffmpeg script based on list of times

    """
    try:
        ffmpeg_scrip_list = []
        number = 0
        for time_start, time_end in times_list:
            time_start = time_start
            time_end = time_end
            number = number + 1
            command = [
                "ffmpeg",
                "-ss", time_start,  # start time
                "-to", time_end,  # end time
                "-i", file_name,  # input file
                "-c", "copy",  # copy the stream
                f"{result_file_name}_{number}.mp4"  # output file
            ]
            ffmpeg_scrip_list.append(command)
        return ffmpeg_scrip_list

    except:
        print(f"Error")
        return []

def makes_ffmpeg_script_from_times(file_name, result_file_name, times, second_before, second_after):
    """
    makes list of ffmpeg script based on list of times
    
    """
    try:
        ffmpeg_scrip_list = []
        for index, time in enumerate(times):
            time_start = subtract_seconds(time, second_before)
            time_end = add_seconds(time, second_after)
            number = index + 1
            command = [
                "ffmpeg",
                "-ss", time_start,  # start time
                "-to", time_end,  # end time
                "-i", file_name,  # input file
                "-c", "copy",  # copy the stream
                f"{result_file_name}_{number}.mp4"  # output file
            ]
            ffmpeg_scrip_list.append(command)
        return ffmpeg_scrip_list

    except:
        print(f"Error")
        return []

def makes_ffmpeg_script_for_summary(file_name, summary_file_name):
    """
    makes list of ffmpeg script based on list of times
    
    """
    try:
        ffmpeg_scrip_list = []
        command = [
            "ffmpeg",
            "-f","concat",  # start time
            "-i", file_name,  # input file
            "-c", "copy",  # copy the stream
            f"{summary_file_name}"  # output file
        ]
        ffmpeg_scrip_list.append(command)
        return ffmpeg_scrip_list

    except:
        print(f"Error")
        return []
    
def generate_ffmpeg_command(input1, input2, output_file, scale_width=1280, encoder="mpeg4", quality=2):
    """
    Generates an FFmpeg command to stack two videos vertically.

    Args:
        input1 (str): Path to the first input video file (e.g., "input1.mp4").
        input2 (str): Path to the second input video file (e.g., "input2.mp4").
        output_file (str): Output file name (e.g., "output.mp4").
        scale_width (int): Width to scale the videos to (default: 1280).
        encoder (str): Video encoder to use (default: "mpeg4").
        quality (int): Quality level for the encoder (default: 2, lower is better).

    Returns:
        list: FFmpeg command as a list of arguments.
    """
    # Base FFmpeg command
    command = ["ffmpeg"]

    # Add input files
    command.extend(["-i", input1])
    command.extend(["-i", input2])

    # Add filter_complex for scaling and stacking
    filter_complex = (
        f"[0:v]scale={scale_width}:-1:flags=lanczos[top];"
        f"[1:v]scale={scale_width}:-1:flags=lanczos[bottom];"
        f"[top][bottom]vstack=inputs=2"
    )
    command.extend(["-filter_complex", filter_complex])

    # Add encoder and quality settings
    command.extend(["-c:v", encoder])
    if encoder == "mpeg4":
        command.extend(["-qscale:v", str(quality)])
    elif encoder == "libx264":
        command.extend(["-crf", str(quality), "-preset", "slow"])

    # Add output file
    command.append(output_file)

    return command

def execute_bash_command(command):
    """
    Trim a video using ffmpeg.

    """
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def write_file_with_numbers(file_name, video_file_name, num_lines):
    with open(file_name, 'w') as file:
        for i in range(1, num_lines + 1):
            file.write(f"file '{video_file_name}_{i}.mp4'\n")

def read_time_ranges(file_path):
    time_ranges = []
    with open(file_path, 'r') as file:
        for line in file:
            start_time, end_time = line.strip().split('-')
            time_ranges.append((start_time, end_time))
    return time_ranges