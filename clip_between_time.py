import functions_list

def main():

    ### CLIPPING
    # get times
    time_list = functions_list.read_time_ranges(FILE_NAME_FOR_INPUT_TIME_BETWEEN)
    print('list of times:')
    print(time_list)

    # write bash scripts for clipping
    scripts = functions_list.makes_ffmpeg_script_from_times_between(FILE_NAME_INPUT_MAIN_VIDEO, FILE_NAME_FOR_PREFIX_RESULT, time_list)
    print('list of scripts:')
    print(scripts)

    # execute bash scripts for clipping
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
    FILE_NAME_INPUT_MAIN_VIDEO = 'source_video/filename.mp4'
    FILE_NAME_FOR_PREFIX_RESULT = 'result_video/clip_game14_2025_between'
    FILE_NAME_FOR_INPUT_TIME_BETWEEN = 'times_between.txt'
    FILE_NAME_FOR_SUMMARY_COMMMAND = 'input_summary_bash.txt'
    FILE_NAME_FOR_SUMMARY = 'result_video/summary_between.mp4'
    main()