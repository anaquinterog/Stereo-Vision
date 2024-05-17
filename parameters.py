"""
parameters.py
Module for storing and manipulating camera calibration parameters,
and for storing and manipulating pixel coordinates.
"""

# Global variables to store pixel coordinates
uL, uR, vL, vR = [], [], [], []

def set_right_pixel_coordinates(pixel_right):
    """
    Convert the given pixel coordinates to lists and store them in the global variables.

    Args:
        pixel_right (list of tuples): The pixel coordinates in the right image.
    """
    global uR, vR
    uR, vR = zip(*pixel_right)
    uR, vR = list(uR), list(vR)  # Convert to lists

def get_right_pixel_coordinates():
    """
    Return the stored pixel coordinates in the right image.

    Returns:
        tuple: The pixel coordinates in the right image.
    """
    return uR, vR

def set_left_pixel_coordinates(pixel_left):
    """
    Convert the given pixel coordinates to lists and store them in the global variables.

    Args:
        pixel_left (list of tuples): The pixel coordinates in the left image.
    """
    global uL, vL
    uL, vL = zip(*pixel_left)
    uL, vL = list(uL), list(vL)  # Convert to lists

def get_left_pixel_coordinates():
    """
    Return the stored pixel coordinates in the left image.

    Returns:
        tuple: The pixel coordinates in the left image.
    """
    return uL, vL

def load_parameters(file_path):
    """
    Load camera calibration parameters from a JSON-like text file.

    Args:
        file_path (str): The path to the file containing the parameters.

    Returns:
        dict: The loaded parameters.
    """
    import json

    with open(file_path, 'r') as f:
        parameters = json.load(f)

    # Extract relevant parameters
    parameters["baseline"] = float(parameters["baseline"])
    parameters["rectified_fx"] = float(parameters["rectified_fx"])
    parameters["rectified_fy"] = float(parameters["rectified_fy"])
    parameters["rectified_cx"] = float(parameters["rectified_cx"])
    parameters["rectified_cy"] = float(parameters["rectified_cy"])
    parameters["rectified_width"] = int(parameters["rectified_width"])
    parameters["rectified_height"] = int(parameters["rectified_height"])

    return parameters

