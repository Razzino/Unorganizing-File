import os
import shutil

folder = r"path/to/your/folder"

def unorganize(folder):
    # Loop through the main folder
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        # If it's a folder, we need to pull files out of it
        if os.path.isdir(item_path):
            for file in os.listdir(item_path):
                file_path = os.path.join(item_path, file)

                # Only move files
                if os.path.isfile(file_path):
                    target = os.path.join(folder, file)
                    shutil.move(file_path, target)  # move file back up

            # After moving files, remove empty folder
            try:
                os.rmdir(item_path)  # removes only if empty
            except OSError:
                pass  # ignore if folder still has content / locked

    print("All files moved back to the main folder.")
    
    
unorganize(r"path/to/your/folder")
# Run the unorganize function
