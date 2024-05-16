import json

uR = [0]*30
vR = [0]*30
uL = [0]*30
vL = [0]*30

TOTALright = [[uR, vR] for _ in range(30)]
TOTALleft = [[uL, vL] for _ in range(30)]

# LOAD PATH TO CALIBRATION PARAMETERS
calibration_file = "/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt"

def load_parameters(file_path):
    """
    Load camera calibration parameters from a JSON-like text file.

    Args:
        file_path (str): Path to the JSON-like text file containing calibration parameters.

    Returns:
        dict: Dictionary containing the loaded calibration parameters.
    """
    # Load camera calibration parameters from the file
    with open(file_path, 'r') as f:
        calibration_data = json.load(f)

    # Extract relevant parameters
    baseline = float(calibration_data["baseline"])
    rectified_fx = float(calibration_data["rectified_fx"])
    rectified_fy = float(calibration_data["rectified_fy"])
    rectified_cx = float(calibration_data["rectified_cx"])
    rectified_cy = float(calibration_data["rectified_cy"])
    rectified_width = int(calibration_data["rectified_width"])
    rectified_height = int(calibration_data["rectified_height"])

    # Create the parameters dictionary
    parameters = {
        "baseline": baseline,
        "rectified_fx": rectified_fx,
        "rectified_fy": rectified_fy,
        "rectified_cx": rectified_cx,
        "rectified_cy": rectified_cy,
        "rectified_width": rectified_width,
        "rectified_height": rectified_height
    }
    """
    # Print the loaded parameters 
    print("Baseline:", parameters["baseline"])
    print("Rectified fx:", parameters["rectified_fx"])
    print("Rectified fy:", parameters["rectified_fy"])
    print("Rectified cx:", parameters["rectified_cx"])
    print("Rectified cy:", parameters["rectified_cy"])
    print("Rectified width:", parameters["rectified_width"])
    print("Rectified height:", parameters["rectified_height"])
"""
    return parameters

parameters = load_parameters(calibration_file)

# Global variables to store pixel coordinates
uL, uR, vL, vR = [], [], [], []

# Function to get pixel coordinates
def get_coordinates():
    global uL, uR, vL, vR
    for i in range(30):
        uL = TOTALleft[i][0]
        vL = TOTALleft[i][1]
        uR = TOTALright[i][0]
        vR = TOTALright[i][1]

    return uL, uR, vL, vR

# Function to set right pixel coordinates
def set_right_pixel_coordinates(pixel_right):
    global uR, vR
    uR, vR = zip(*pixel_right)

    print("\nPixel coordinates of selected points in the right image:")
    for point in pixel_right:
        print(point)

# Function to get right pixel coordinates
def get_right_pixel_coordinates():
    return uR, vR

# Function to set left pixel coordinates
def set_left_pixel_coordinates(pixel_left):
    global uL, vL
    uL, vL = zip(*pixel_left)

    # Print the pixel coordinates saved for the left and right images
    print("Pixel coordinates of selected points in the left image:")
    for point in pixel_left:
        print(point)

# Function to get left pixel coordinates
def get_left_pixel_coordinates():
    return uL, vL
