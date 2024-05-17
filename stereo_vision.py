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
python -u "/Users/anabi/Documents/GitHub/stereo-vision/stereo_vision.py" --l_img "/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png" --r_img "/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png"

"""

# Importing the necessary libraries
import cv2 as cv
import argparse
import calculations as calc
import parameters as param

# Global variables to store pixel coordinates and point counter for left and right images
pixel_left = []
pixel_right = []
point_counter_left = 0
point_counter_right = 0

def parse_args():
    """
    Parse command line arguments for image paths.

    Returns:
        Namespace: Parsed command line arguments with paths to the images.
    """
    parser = argparse.ArgumentParser(description='Stereo Calibration')
    parser.add_argument('--l_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png", help='Path to the left image')
    parser.add_argument('--r_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png", help='Path to the right image')
    args = parser.parse_args()
    return args

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

def pipeline():
    """
    Main function to run the stereo vision pipeline.

    This function loads the left and right images, resizes them,
    creates windows for the images, sets mouse callbacks,
    displays the images, collects pixel coordinates, calculates
    3D points, and displays the 3D points.
    """
    # Load calibration parameters
    parameters_data = param.load_parameters("/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt")

    # Parse command line arguments
    args = parse_args()

    # Load left and right images
    left_image = cv.imread(args.l_img)
    right_image = cv.imread(args.r_img)

    # Resize images
    scale_factor = 0.75
    left_image_resized = cv.resize(left_image, None, fx=scale_factor, fy=scale_factor)
    right_image_resized = cv.resize(right_image, None, fx=scale_factor, fy=scale_factor)

    # Create windows and set mouse callback for left and right images
    cv.namedWindow('Left Infrared Image')
    cv.setMouseCallback('Left Infrared Image', mouse_callback_left, {'image_left': left_image_resized, 'window_name_left': 'Left Infrared Image'})

    cv.namedWindow('Right Infrared Image')
    cv.setMouseCallback('Right Infrared Image', mouse_callback_right, {'image_right': right_image_resized, 'window_name_right': 'Right Infrared Image'})

    # Display images
    cv.imshow('Left Infrared Image', left_image_resized)
    cv.imshow('Right Infrared Image', right_image_resized)

    print("Left click on the images to add a dot. Press 'q' to quit.")

    # Collect pixel coordinates until 30 points are selected from each image
    while len(pixel_left) < 30 or len(pixel_right) < 30:
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv.destroyAllWindows()

    # If enough points are selected, calculate and display 3D points
    if len(pixel_left) == 30 and len(pixel_right) == 30:
        # Set pixel coordinates
        param.set_left_pixel_coordinates(pixel_left)
        param.set_right_pixel_coordinates(pixel_right)

        # Get pixel coordinates
        uL, vL = param.get_left_pixel_coordinates()
        uR, vR = param.get_right_pixel_coordinates()

        # Calculate 3D points
        X, Y, Z = calc.calculate_coordinates(uL, uR, vL, vR, parameters_data)

        # Display 3D points
        calc.display_points(X, Y, Z)
    else:
        print("Not enough points selected.")

if __name__ == '__main__':
    pipeline()
