import os
import pathlib

def process_wav_files(root_dir):
    """
    Finds .wav files in subfolders of a directory, lists their sizes,
    and deletes those larger than 500KB.

    Args:
        root_dir (str): The root directory to search in.
    """

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".mp3"):
                filepath = os.path.join(subdir, file)
                file_size_kb = os.path.getsize(filepath) / 1024  # Size in KB
                print(f"File: {filepath}, Size: {file_size_kb:.2f} KB")

                if file_size_kb > 900:
                    try:
                        os.remove(filepath)
                        print(f"  Deleted: {filepath}")
                    except OSError as e:
                        print(f"  Error deleting {filepath}: {e}")


if __name__ == "__main__":
    root_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voice of Birds"  # Use raw string

    process_wav_files(root_directory)