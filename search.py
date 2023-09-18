import os
from moviepy.editor import AudioFileClip, concatenate_audioclips

# Define the root directory as the current directory (where the script is located)
root_directory = "."

# Function to create a .txt file with a list of .mp3 files in a folder
def create_txt_file(folder_path, mp3_files):
    folder_name = os.path.basename(folder_path)
    txt_filename = os.path.join(folder_path, folder_name + ".txt")
    with open(txt_filename, "w") as txt_file:
        for mp3_file in mp3_files:
            txt_file.write(mp3_file + "\n")

# Function to combine all .mp3 files in a folder into one
def combine_mp3_files(folder_path, mp3_files):
    audio_clips = []
    for mp3_file in mp3_files:
        mp3_path = os.path.join(folder_path, mp3_file)
        audio_clip = AudioFileClip(mp3_path)
        audio_clips.append(audio_clip)
    combined_audio = concatenate_audioclips(audio_clips)
    combined_audio.write_audiofile(os.path.join(folder_path, "combined.mp3"), codec="mp3")

# Iterate through all directories and subdirectories within the root directory
for folder_path, _, files in os.walk(root_directory):
    mp3_files = [file for file in files if file.endswith(".mp3")]
    if mp3_files:
        create_txt_file(folder_path, mp3_files)  # Create .txt file with a list of .mp3 files
        combine_mp3_files(folder_path, mp3_files)  # Combine .mp3 files into one
        print(f"Created .txt and combined .mp3 in {os.path.basename(folder_path)}")

print("Done!")
