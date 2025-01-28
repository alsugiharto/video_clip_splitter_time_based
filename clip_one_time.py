import functions_list

def main():
    ### CLIPPING

    # get times
    times = functions_list.read_times_from_file(FILE_NAME_FOR_INPUT_TIME_ONE)
    print('list of times:')
    print(times)

    # write all the scripts
    scripts = functions_list.makes_ffmpeg_script_from_times(FILE_NAME_INPUT_MAIN_VIDEO, FILE_NAME_FOR_PREFIX_RESULT, times, SECOND_BEFORE, SECOND_AFTER)
    print('list of scripts:')
    print(scripts)

    # execute the scripts
    print('executing clipping...')
    number_of_videos = len(scripts)
    for script in scripts:
        functions_list.execute_bash_command(script)

    ### SUMMARY

    # prepare input for summary
    functions_list.write_file_with_numbers(FILE_NAME_FOR_SUMMARY_COMMMAND, FILE_NAME_FOR_PREFIX_RESULT, number_of_videos)
    # prepare bash scripts for summary
    print('summary')
    command_for_summary = functions_list.makes_ffmpeg_script_for_summary(FILE_NAME_FOR_SUMMARY_COMMMAND,FILE_NAME_FOR_SUMMARY)
    print(command_for_summary)
    print('executing summary...')
    # execute bash scripts for summary
    for script in command_for_summary:
        functions_list.execute_bash_command(script)

if __name__ == "__main__":
    FILE_NAME_INPUT_MAIN_VIDEO = 'source_video/filename2.mp4'
    FILE_NAME_FOR_PREFIX_RESULT = 'result_video/clip_game14_2025'
    FILE_NAME_FOR_SUMMARY = 'result_video/summary_game14_2025.mp4'
    FILE_NAME_FOR_INPUT_TIME_ONE = 'times_one.txt'
    FILE_NAME_FOR_SUMMARY_COMMMAND = 'input_summary_bash.txt'
    SECOND_BEFORE = 7
    SECOND_AFTER = 4
    main()