import os
from PIL import Image

def destroy(input_dir, output_dir):
    """
    Splits each PNG image in the input directory into 8 parts (4 rows x 2 columns)
    and saves the parts in the output directory.

    Args:
        input_dir (str): Path to the directory containing PNG images.
        output_dir (str): Path to the directory where the image parts will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    img_no = 1
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(input_dir, filename)
            with Image.open(image_path) as img:
                width, height = img.size

                # Determine the size of each part
                part_width = width // 2
                part_height = height // 4

                # Split the image into 8 parts (4 rows x 2 columns)
                part_number = 1
                for row in range(4):
                    for col in range(2):
                        left = col * part_width
                        upper = row * part_height
                        right = left + part_width
                        lower = upper + part_height

                        part = img.crop((left, upper, right, lower))

                        # Save the part to the output directory
                        part_filename = f"{os.path.splitext(filename)[0]}_part{part_number}.png"
                        part.save(os.path.join(output_dir, part_filename))

                        part_number += 1
                        
                        print(img_no, part_number, end='\r')
            img_no += 1

# Example usage:
input_directory = "LR1"
output_directory = "LR"
destroy(input_directory, output_directory)
