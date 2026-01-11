import os
import zipfile

def find_subfolders_with_more_than_n_files(root_dir):

    results = []
    for subdir, _, files in os.walk(root_dir):
        #print(subdir)
        for file in files:
            if file.lower().endswith(".zip"):
                folder_name = os.path.splitext(file)[0]
                extract_path = os.path.join(subdir, folder_name)
                os.makedirs(extract_path, exist_ok=True)
                file_path = os.path.join(subdir, file)
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
            print(f"Unzipped: {file_path} to {extract_path}")
        
        print(f"{file}\n")
    return results


if __name__ == "__main__":
    root_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voices"

    #subfolders = find_subfolders_with_more_than_n_files(root_directory)
    for subdir, _, files in os.walk(root_directory):
        file_count = len(files)
        print(f"Subfolder: {subdir.split('\\')[-1]}, File count: {file_count}")
        #print(f"Subfolder: {subdir.split("\")[-1]}, File count: {file_count}")


    voice_folder = os.path.join(root_directory, "voice")
    os.makedirs(voice_folder, exist_ok=True)
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".wav"):
                source_path = os.path.join(subdir, file)
                destination_path = os.path.join(voice_folder, file)
                os.rename(source_path, destination_path)
                print(f"Moved: {source_path} to {destination_path}")
