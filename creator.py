import os
from PIL import Image

def create(parts_dir, output_dir):
    """
    Reconstructs the original images from their parts stored in the specified directory.

    Args:
        parts_dir (str): Path to the directory containing image parts.
        output_dir (str): Path to the directory where reconstructed images will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = {}

    # Group parts by original image name
    for filename in os.listdir(parts_dir):
        if filename.endswith('.png') and '_part' in filename:
            base_name, part_info = filename.rsplit('_part', 1)
            part_number = int(part_info.split('.')[0])

            if base_name not in images:
                images[base_name] = {}

            images[base_name][part_number] = os.path.join(parts_dir, filename)

    # Reconstruct each image
    for base_name, parts in images.items():
        # Sort parts by their part number
        sorted_parts = [parts[i] for i in sorted(parts)]

        # Open the first part to get the dimensions
        with Image.open(sorted_parts[0]) as part_img:
            part_width, part_height = part_img.size

        reconstructed_width = part_width * 2
        reconstructed_height = part_height * 4

        reconstructed_image = Image.new('RGB', (reconstructed_width, reconstructed_height))

        part_number = 0
        for row in range(4):
            for col in range(2):
                with Image.open(sorted_parts[part_number]) as part_img:
                    left = col * part_width
                    upper = row * part_height
                    reconstructed_image.paste(part_img, (left, upper))
                part_number += 1

        # Save the reconstructed image
        output_path = os.path.join(output_dir, f"{base_name}.png")
        reconstructed_image.save(output_path)


parts_directory = "path/to/your/parts_directory"
reconstructed_directory = "path/to/your/reconstructed_directory"
create4(parts_directory, reconstructed_directory)
