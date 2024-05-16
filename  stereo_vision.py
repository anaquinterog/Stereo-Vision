"""
MAIN PYTHON SCRIPT
stereo-vision.py
Homework 11: Sparse 3D reconstruction using stereo vision.

Authors:  Ana Bárbara Quintero 544073
Organisation: UDEM
Due date: Thursday, May 16th, 2024

EXAMPLE TERMINAL CODE: 
$ python stereo_vision.py --l_img left-image.png --r_img right-image.png

MY TERMINAL CODE:
python -u "/Users/anabi/Documents/GitHub/stereo-vision/ stereo_vision.py" --l_img "/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png" --r_img "/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png"

"""

# Importing the necessary libraries
import cv2 as cv
import argparse
import calculations as calc
import parameters as param
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import point_visualizer 

# Global variables to store pixel coordinates and point counter for left and right images
pixel_left = []
pixel_right = []
point_counter_left = 0
point_counter_right = 0


uR = [0]*30
vR = [0]*30
uL = [0]*30
vL = [0]*30



def parse_args():
    """
    Parse command line arguments for image paths.
    
    This function parses the command line arguments for the paths to the image file for object detection
    and the video file. The function returns a Namespace object containing the parsed arguments.

    Returns:
        Namespace: Parsed command line arguments with paths to the images.
    """

    parser = argparse.ArgumentParser(description='Stereo Calibration')
    parser.add_argument('--l_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png", help='Path to the left image')
    parser.add_argument('--r_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png", help='Path to the right image')
    args = parser.parse_args()


    return args


def get_coordinates():
    
    global uL, uR, vL, vR
    uL = [0] * 30
    uR = [0] * 30
    vL = [0] * 30
    vR = [0] * 30    
    
    global pixel_left, pixel_right
    """
    if event == cv.EVENT_LBUTTONDOWN:
        if param == 'left':
            uL, v = x, y
        elif param == 'right':
            uR = x"""
    
    

    return uL, uR, vL, vR


def mouse_callback_left(event, x, y, flags, param):
    """
    Mouse callback function to handle mouse events for the left image.

    Args:
        event (int): Type of mouse event.
        x (int): x-coordinate of the mouse cursor.
        y (int): y-coordinate of the mouse cursor.
        flags (int): Additional flags.
        param (dict): Additional parameters.
    """
    global pixel_left, point_counter_left

    if event == cv.EVENT_LBUTTONDOWN:
        # Check if the point counter exceeds the limit (30 points)
        if point_counter_left >= 30:
            print("Maximum point limit reached for the left image (30 points).")
            return

        # Save pixel coordinates for the left image
        pixel_left.append((x, y))

        # Draw dot on the left image
        cv.circle(param['image_left'], (x, y), 3, (0, 0, 255), -1)

        # Increment the point counter for the left image
        point_counter_left += 1

        # Clear the previous text by filling a rectangle with the background color
        cv.rectangle(param['image_left'], (0, 0), (600, 40), (255, 255, 255), -1)

        # Update the text for the left image
        text_left = f"Selected points (Left): {point_counter_left}/30"
        cv.putText(param['image_left'], text_left, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)

        # Show the updated left image
        cv.imshow(param['window_name_left'], param['image_left'])

def mouse_callback_right(event, x, y, flags, param):
    """
    Mouse callback function to handle mouse events for the right image.

    Args:
        event (int): Type of mouse event.
        x (int): x-coordinate of the mouse cursor.
        y (int): y-coordinate of the mouse cursor.
        flags (int): Additional flags.
        param (dict): Additional parameters.
    """
    global pixel_right, point_counter_right

    if event == cv.EVENT_LBUTTONDOWN:
        # Check if the point counter exceeds the limit (30 points)
        if point_counter_right >= 30:
            print("Maximum point limit reached for the right image (30 points).")
            return

        # Save pixel coordinates for the right image
        pixel_right.append((x, y))

        # Draw dot on the right image
        cv.circle(param['image_right'], (x, y), 3, (0, 0, 255), -1)

        # Increment the point counter for the right image
        point_counter_right += 1

        # Clear the previous text by filling a rectangle with the background color
        cv.rectangle(param['image_right'], (0, 0), (600, 40), (255, 255, 255), -1)

        # Update the text for the right image
        text_right = f"Selected points (Right): {point_counter_right}/30"
        cv.putText(param['image_right'], text_right, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)

        # Show the updated right image
        cv.imshow(param['window_name_right'], param['image_right'])




if __name__ == '__main__':
    # Parse command line arguments
    args = parse_args()

    # Create an empty list to store points
    pointsR = []
    pointsL = []

    # Load left and right images
    left_image = cv.imread(args.l_img)
    right_image = cv.imread(args.r_img)

    # Resize the images for better display
    scale_factor = 0.5
    left_image_resized = cv.resize(left_image, None, fx=scale_factor, fy=scale_factor)
    right_image_resized = cv.resize(right_image, None, fx=scale_factor, fy=scale_factor)
    
    # Create windows to display the left and right images
    cv.namedWindow("Left Image")
    cv.namedWindow("Right Image")
    
    # Set mouse callback functions for the left and right images
    cv.setMouseCallback("Left Image", mouse_callback_left, {'image_left': left_image_resized, 'window_name_left': 'Left Image'})
    cv.setMouseCallback("Right Image", mouse_callback_right, {'image_right': right_image_resized, 'window_name_right': 'Right Image'})
    
    # Display the left and right images
    cv.imshow("Left Image", left_image_resized)
    cv.imshow("Right Image", right_image_resized)
    
    cv.waitKey(0)
    cv.destroyAllWindows()


    # Set the right pixel coordinates in the parameters module
    param.set_right_pixel_coordinates(pixel_right)
    param.set_left_pixel_coordinates(pixel_left)

    # Display the points in 3D

    X = [0] * 30
    Y = [0] * 30
    Z = [0] * 30

    parameters_data = param.load_parameters("/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt")
    for i in range(30):
        uL[i], uR[i], vL[i], vR[i] = param.get_coordinates()

        X[i], Y[i], Z[i] = calc.calculate_coordinates(uL[i], uR[i], vL[i], vR[i], parameters_data)

        point_visualizer.display_points(X, Y, Z)



