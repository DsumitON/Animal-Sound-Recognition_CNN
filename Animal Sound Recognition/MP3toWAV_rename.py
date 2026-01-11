import os

def rename_mp3_to_wav(input_folder):
    """Renames .mp3 files to .wav within subfolders."""

    for subfolder_name in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder_name)

        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                if filename.lower().endswith(".m4a"):
                    old_file = os.path.join(subfolder_path, filename)
                    new_file = os.path.join(subfolder_path, os.path.splitext(filename)[0] + ".wav")

                    try:
                        os.rename(old_file, new_file)
                        print(f"Renamed: {old_file} to {new_file}")
                    except FileNotFoundError:
                        print(f"File not found: {old_file}")
                    except FileExistsError:
                        print(f"File already exists: {new_file}")

if __name__ == "__main__":
    input_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voices"
    rename_mp3_to_wav(input_directory)