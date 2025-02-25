'''
This script is used to store drawings (in png format) from the `analysis/data/drawings/png` 
directory into the `user_images` directory in this repository. 
'''

import os
import shutil

ROOT_IMAGE_DIR = "../../data/drawings/png"
SAVE_IMAGE_DIR = "user_images"

def main():
    # Create save directory if it doesn't exist
    os.makedirs(SAVE_IMAGE_DIR, exist_ok=True)
    
    # Get all the batch folders in the `analysis/data/drawings/png` directory
    batch_folders = [os.path.join(ROOT_IMAGE_DIR, batch) for batch in os.listdir(ROOT_IMAGE_DIR) 
                    if os.path.isdir(os.path.join(ROOT_IMAGE_DIR, batch))]

    for batch_folder in batch_folders:
        print(f"Processing {os.path.basename(batch_folder)}...")
        
        # Get all the png files in the batch folder
        png_files = [f for f in os.listdir(batch_folder) if f.endswith('.png')]
        
        # Copy each png file to the user_images directory
        for png_file in png_files:
            src = os.path.join(batch_folder, png_file)
            dst = os.path.join(SAVE_IMAGE_DIR, png_file)
            
            try:
                shutil.copy2(src, dst)  # copy2 preserves metadata
            except Exception as e:
                print(f"Error copying {png_file}: {str(e)}")
                
        print(f"Copied {len(png_files)} images from {os.path.basename(batch_folder)}")

if __name__ == "__main__":
    main()

# Example usage
# python store_user_images.py
