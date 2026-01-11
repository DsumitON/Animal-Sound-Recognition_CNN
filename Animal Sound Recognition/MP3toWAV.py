import os
import subprocess

def convert_mp3_to_wav(input_folder, output_folder):
    """Converts MP3 files to WAV files within subfolders."""

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for subfolder_name in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder_name)

        if os.path.isdir(subfolder_path):
            output_subfolder = os.path.join(output_folder, subfolder_name)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)

            for filename in os.listdir(subfolder_path):
                if filename.lower().endswith(".mp3"):
                    input_file = os.path.join(subfolder_path, filename)
                    output_file = os.path.join(output_subfolder, os.path.splitext(filename)[0] + ".wav")

                    try:
                        subprocess.run(['ffmpeg', '-i', input_file, output_file], check=True)
                        print(f"Converted: {input_file} to {output_file}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error converting {input_file}: {e}")
                    except FileNotFoundError:
                        print("ffmpeg not found. Please install ffmpeg and ensure it's in your PATH.")
                        return

if __name__ == "__main__":
    input_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voice of Birds"
    output_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voice of Birds_wav" #output directory
    convert_mp3_to_wav(input_directory, output_directory)