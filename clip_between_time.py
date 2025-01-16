import functions_list

def read_time_ranges(file_path):
    time_ranges = []
    with open(file_path, 'r') as file:
        for line in file:
            start_time, end_time = line.strip().split('-')
            time_ranges.append((start_time, end_time))
    return time_ranges

def main():
    # get times
    time_list = read_time_ranges(FILE_TIME_PATH)
    print('list of times:')
    print(time_list)

    # write all the scripts
    scripts = functions_list.makes_ffmpeg_script_from_times_between(FILE_NAME, RESULT_FILE_NAME, time_list)
    print('list of scripts:')
    print(scripts)

    # execute the scripts
    print('executing...')
    for script in scripts:
        functions_list.execute_bash_command(script)

if __name__ == "__main__":
    FILE_NAME = 'filename.mp4'
    RESULT_FILE_NAME = 'clip_game14_2025_between'
    FILE_TIME_PATH = 'times_between.txt'
    main()