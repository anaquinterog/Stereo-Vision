import parameters as param # Import parameters.py file
#import stereovision as sv # Import stereo_vision.py file



def calculate_coordinates(uL, uR, vL, vR, parameters):
    """
    Calculate 3D coordinates (X, Y, Z) from pixel coordinates and camera parameters.

    Args:
        uL (float): u-coordinate of the left image pixel.
        uR (float): u-coordinate of the right image pixel.
        vL (float): v-coordinate of the left image pixel.
        vR (float): v-coordinate of the right image pixel.
        parameters (dict): Camera calibration parameters.

    Returns:
        tuple: Tuple containing the calculated X, Y, and Z coordinates.
    """
    
    ucL = uL - parameters["rectified_cx"] 
    vcL = vL - parameters["rectified_cy"] 
 
    ucR = uR - parameters["rectified_cx"] 
    vcR = vR - parameters["rectified_cy"] 


    d = ucL - ucR

    Z = parameters["rectified_fx"] * (parameters["baseline"] / d) #  f * B / d 
    X = ucL * Z / parameters["rectified_fx"]
    Y = vcL * Z / parameters["rectified_fy"]

    print("X, Y, Z = {:.5f} {:.5f} {:.5f}".format(X, Y, Z))

    return X, Y, Z

global X, Y, Z
##WRITE IN CODE FOR PARAMETERS
parameters = param.load_parameters("/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt")
uL, uR, vL, vR = param.get_coordinates()
X, Y, Z = calculate_coordinates(uL, uR, vL, vR, parameters)
