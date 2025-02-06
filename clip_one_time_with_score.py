import functions_write_score_list
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

    # prepare command input for summary
    functions_list.write_file_with_numbers_with_score(FILE_NAME_FOR_SUMMARY_COMMMAND, FILE_NAME_FOR_PREFIX_RESULT, number_of_videos, FILE_NAME_POSTFIX_FOR_SCORE)
    # prepare bash scripts for summary

    print('creating score')
    who_score = functions_write_score_list.read_who_scores_from_file(FILE_NAME_FOR_INPUT_WHO_SCORE)
    times = functions_list.read_times_from_file(FILE_NAME_FOR_INPUT_TIME_ONE)
    #TODO: check if number between who score and times are the same
    functions_write_score_list.add_text_to_video(FILE_NAME_FOR_PREFIX_RESULT, FILE_NAME_POSTFIX_FOR_SCORE, times, who_score)

    print('creating summary')
    command_for_summary = functions_list.makes_ffmpeg_script_for_summary(FILE_NAME_FOR_SUMMARY_COMMMAND,FILE_NAME_FOR_SUMMARY)
    print(command_for_summary)
    print('executing summary...')
    # execute bash scripts for summary
    for script in command_for_summary:
        functions_list.execute_bash_command(script)

if __name__ == "__main__":
    FILE_NAME_INPUT_MAIN_VIDEO = 'source_video/filename.mp4'
    FILE_NAME_FOR_PREFIX_RESULT = 'result_video/clip_game14_2025'
    FILE_NAME_FOR_SUMMARY = 'result_video/summary_with_score.mp4'
    FILE_NAME_FOR_INPUT_TIME_ONE = 'times_one.txt'
    FILE_NAME_FOR_INPUT_WHO_SCORE = 'who_score.txt'
    FILE_NAME_FOR_INPUT_TIME_ONE = 'times_one.txt'
    FILE_NAME_FOR_SUMMARY_COMMMAND = 'input_summary_with_score_bash.txt'
    FILE_NAME_POSTFIX_FOR_SCORE = 'with_score'
    SECOND_BEFORE = 7
    SECOND_AFTER = 4
    main()



