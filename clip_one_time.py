import functions_list

def main():
    # get times

    times = functions_list.read_times_from_file(FILE_TIME_PATH)
    print('list of times:')
    print(times)

    # write all the scripts
    scripts = functions_list.makes_ffmpeg_script_from_times(FILE_NAME, RESULT_FILE_NAME, times, SECOND_BEFORE, SECOND_AFTER)
    print('list of scripts:')
    print(scripts)

    # execute the scripts
    print('executing...')
    for script in scripts:
        functions_list.execute_bash_command(script)

if __name__ == "__main__":
    FILE_NAME = 'filename.mp4'
    RESULT_FILE_NAME = 'clip_game14_2025'
    FILE_TIME_PATH = 'times_one.txt'
    SECOND_BEFORE = 7
    SECOND_AFTER = 4
    main()