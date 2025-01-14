import cv2 as cv
import random as rand

def interpolation_method():
    methods = [
        cv.INTER_AREA,
        cv.INTER_LINEAR,
        cv.INTER_LANCZOS4,
        cv.INTER_CUBIC,
        cv.INTER_NEAREST,
    ]
    return methods[(rand.randint(0, len(methods) - 1))]
    
def down_sample(img_path:str):
    """down sample the image based on various interpolation methods

    Args:
        img_path (str): path to the image
    """
    try:
        image = cv.imread(img_path)
    except Exception as e:
        print(e)
    if rand.random() < 0.5:
        image = cv.resize(image, dsize=(256, 192), interpolation=interpolation_method())
    else:
        image = cv.resize(image, dsize=(2 * 256, 2 * 192), interpolation=interpolation_method())
        image = cv.resize(image, dsize=(256, 192), interpolation=interpolation_method())
    return image


if __name__ == '__main__':
    import os
    data_dir = os.path.join(os.path.dirname(__file__), 'Flickr2K_HR')
    LR_dir = os.path.join(os.path.dirname(__file__), 'HR')
    
    for i in range(1, 2651):
        read_img_number = f'{str(i).zfill(6)}.png'
        img_file = os.path.join(data_dir, read_img_number)
        image = down_sample(img_file)
        img_number = f'{str(i+900).zfill(4)}.png'

        if not cv.imwrite(os.path.join(LR_dir, img_number), image):
            print(f"There was some error writing this file: {img_number}")
        print(f"{img_number} saved to LR/", end='\r')