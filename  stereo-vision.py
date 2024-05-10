"""
MAIN PYTHON SCRIPT
stereo-vision.py
Homework 11: Sparse 3D reconstruction using stereo vision.

Authors:  Ana Bárbara Quintero 544073
Organisation: UDEM
Due date: Thursday, May 16th, 2024

EXAMPLE TERMINAL CODE: 
$ python stereo-vision.py --l_img left-image.png --r_img right-image.png

MY TERMINAL CODE:
python -u "/Users/anabi/Documents/GitHub/stereo-vision/ stereo-vision.py" --l_img "/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png" --r_img "/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png"

"""
# Importing the necessary libraries
import cv2 as cv
import argparse

def parse_args():
    """
    Parse command line arguments for image paths.
    
    This function parses the command line arguments for the paths to the image file for object detection
    and the video file. The function returns a Namespace object containing the parsed arguments.

    Returns:
        Namespace: Parsed command line arguments with paths to the images.
    """
    parser = argparse.ArgumentParser(description='View left and right images')
    parser.add_argument('--l_img', required=True,
                        help='Path for LEFT image')
    parser.add_argument('--r_img', required=True,
                        help='Path for RIGHT image')
    args = parser.parse_args()
    return args

def run_pipeline(video_path, img_obj_path):
  



    return 


def display_images(left_image, right_image):
    """
    Display left and right images side by side.
    
    Args:
        left_image (numpy.ndarray): Left image array.
        right_image (numpy.ndarray): Right image array.
    """
    # Resize images to the same height (assuming both have the same height)
    height = max(left_image.shape[0], right_image.shape[0])
    left_image_resized = cv.resize(left_image, (int(left_image.shape[1] * height / left_image.shape[0]), height))
    right_image_resized = cv.resize(right_image, (int(right_image.shape[1] * height / right_image.shape[0]), height))
    
    # Display images side by side
    concatenated_image = cv.hconcat([left_image_resized, right_image_resized])
    cv.imshow('Stereo Vision', concatenated_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    # Parse command line arguments
    args = parse_args()

    # Load left and right images
    left_image = cv.imread(args.l_img)
    right_image = cv.imread(args.r_img)

    # Display left and right images
    cv.imshow('Left Image', left_image)
    cv.imshow('Right Image', right_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


