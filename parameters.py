import json

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


def get_coordinates():
    
    global uL, uR, vL, vR
    uL = 670
    uR = 588
    vL  = 442
    vR = 442

    return uL, uR, vL, vR