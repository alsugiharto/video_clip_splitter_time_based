import functions_write_score_list
import functions_list

def main():
    who_score = functions_write_score_list.read_who_scores_from_file(FILE_NAME_FOR_INPUT_WHO_SCORE)
    times = functions_list.read_times_from_file(FILE_NAME_FOR_INPUT_TIME_ONE)
    #TODO: check if number between who score and times are the same
    functions_write_score_list.add_text_to_video(FILE_NAME_FOR_SUMMARY, times, who_score)

if __name__ == "__main__":
    FILE_NAME_FOR_SUMMARY = 'result_video/clip_game14_2025'
    FILE_NAME_FOR_INPUT_TIME_ONE = 'times_one.txt'
    FILE_NAME_FOR_INPUT_WHO_SCORE = 'who_score.txt'
    main()