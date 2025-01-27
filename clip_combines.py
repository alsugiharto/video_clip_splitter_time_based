import functions_list

def main():
    ### combine

    # Example usage
    ffmpeg_scrip_list = []

    # Generate the command
    command = functions_list.generate_ffmpeg_command(
        input1=FILE_NAME_INPUT_1,
        input2=FILE_NAME_INPUT_2,
        output_file=FILE_NAME_OUTPUT,
        encoder="mpeg4",
        quality=2
    )
    ffmpeg_scrip_list.append(command)

    print('command_for_summary')
    print('executing summary...')
    # execute bash scripts for summary
    for script in ffmpeg_scrip_list:
        functions_list.execute_bash_command(script)

if __name__ == "__main__":
    FILE_NAME_INPUT_1 = 'input1.mp4'
    FILE_NAME_INPUT_2 = 'input2.mp4'
    FILE_NAME_OUTPUT = 'summary_combine_one.mp4'
    main()