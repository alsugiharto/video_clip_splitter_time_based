import re
from datetime import datetime, timedelta
import subprocess

SECOND_BEFORE = 7
SECOND_AFTER = 4
FILE_NAME = 'filename.mp4'
FILE_PATH = 'times.txt'

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
    
from datetime import datetime, timedelta

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

def makes_ffmpeg_script_from_times(times):
    """
    makes list of ffmpeg script based on list of times
    
    """
    try:
        ffmpeg_scrip_list = []
        for index, time in enumerate(times):
            time_start = subtract_seconds(time, SECOND_BEFORE)
            time_end = add_seconds(time, SECOND_AFTER)
            number = index + 1
            command = [
                "ffmpeg",
                "-ss", time_start,  # start time
                "-to", time_end,  # end time
                "-i", FILE_NAME,  # input file
                "-c", "copy",  # copy the stream
                f"result{number}.mp4"  # output file
            ]
            ffmpeg_scrip_list.append(command)
        return ffmpeg_scrip_list

    except:
        print(f"Error")
        return []

def execute_bash_command(command):
    """
    Trim a video using ffmpeg.

    """
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# get times
times = read_times_from_file(FILE_PATH)
print(times)

# write all the scripts
scripts = makes_ffmpeg_script_from_times(times)
print(scripts)

# execute the scripts
for script in scripts:
    execute_bash_command(script)