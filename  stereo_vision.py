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
##?? import parameters as param 
import calculations as calc


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
    
    global uL, uR, v
    """
    if event == cv.EVENT_LBUTTONDOWN:
        if param == 'left':
            uL, v = x, y
        elif param == 'right':
            uR = x"""
    
    #return ... for now
    uL = 670
    uR = 588
    vL  = 442
    vR = 442

    return uL, uR, v



def display_images(left_image, right_image, scale_factor):
    """
    Display left and right images (resized) and draw dots on each image as the user clicks.

    Args:
        left_image (numpy.ndarray): Left infrared image.
        right_image (numpy.ndarray): Right infrared image.
        scale_factor (float): Scale factor for resizing images. Default is 0.5 (50% of original size).
    """
    # Resize images
    left_image_resized = cv.resize(left_image, None, fx=scale_factor, fy=scale_factor)
    right_image_resized = cv.resize(right_image, None, fx=scale_factor, fy=scale_factor)

    # Create empty lists to store points for left and right images
    left_points = []
    right_points = []

    def draw_dots(image, points):
        """
        Draw red dots on the image at specified points.

        Args:
            image (numpy.ndarray): Input image.
            points (list): List of (x, y) coordinates of points.

        Returns:
            numpy.ndarray: Image with red dots drawn.
        """
        dot_radius = 3
        dot_color = (0, 0, 255)  # Red color in BGR format
        for point in points:
            cv.circle(image, point, dot_radius, dot_color, -1)
        return image

    def mouse_callback(event, x, y, flags, param):
        """
        Mouse callback function to handle mouse events.

        Args:
            event (int): Type of mouse event.
            x (int): x-coordinate of the mouse cursor.
            y (int): y-coordinate of the mouse cursor.
            flags (int): Additional flags.
            param (dict): Additional parameters.
        """
        image_type = param['image_type']
        if image_type == 'left':
            points = left_points
        elif image_type == 'right':
            points = right_points

        if event == cv.EVENT_LBUTTONDOWN:
            points.append((x, y))
            draw_dots(param['image'], points)
            cv.imshow(param['window_name'], param['image'])

    # Create windows and set mouse callback for left and right images
    cv.namedWindow('Left Infrared Image')
    cv.setMouseCallback('Left Infrared Image', mouse_callback, {'image': left_image_resized, 'image_type': 'left', 'window_name': 'Left Infrared Image'})

    cv.namedWindow('Right Infrared Image')
    cv.setMouseCallback('Right Infrared Image', mouse_callback, {'image': right_image_resized, 'image_type': 'right', 'window_name': 'Right Infrared Image'})

    # Display left and right images
    cv.imshow('Left Infrared Image', left_image_resized)
    cv.imshow('Right Infrared Image', right_image_resized)

    print("Left click on the left image to add a dot. Press 'q' to quit.")

    while True:
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv.destroyAllWindows()






if __name__ == '__main__':
    # Parse command line arguments
    args = parse_args()

    # Create an empty list to store points
    pointsR = []
    pointsL = []

    # Load left and right images
    left_image = cv.imread(args.l_img)
    right_image = cv.imread(args.r_img)

    # Resize images
    scale_factor = 0.75
    display_images(left_image, right_image, scale_factor)
    




    


