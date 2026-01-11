import os

def find_subfolders_with_more_than_n_files(root_dir, n):
    """
    Finds subfolders in a directory that contain more than n files.

    Args:
        root_dir (str): The root directory to search in.
        n (int): The minimum number of files a subfolder must have.
    """

    results = []
    for subdir, _, files in os.walk(root_dir):
        if subdir != root_dir: # Exclude the root directory itself
            if len(files) > n:
                results.append(subdir)
    return results

if __name__ == "__main__":
    root_directory = r"C:\Users\Sumit\ownCloud\Documents\AppliedSignalProcessing\Voice of Birds"
    min_files = 25

    subfolders = find_subfolders_with_more_than_n_files(root_directory, min_files)

    if subfolders:
        print(f"Subfolders with more than {min_files} files:")
        for folder in subfolders:
            print(folder)
    else:
        print(f"No subfolders found with more than {min_files} files.")