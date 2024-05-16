import parameters  # Import parameters.py file
import numpy as np

uR = [0]*30
vR = [0]*30
uL = [0]*30
vL = [0]*30

ucL = [0] * 30
vcL = [0] * 30
ucR = [0] * 30
vcR = [0] * 30
d = [1] * 30

Z = [0] * 30
X = [0] * 30
Y = [0] * 30



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

    for i in range(30):
        ucL[i] = uL[i] - parameters["rectified_cx"] 
        vcL[i] = vL[i] - parameters["rectified_cy"] 
    
        ucR[i] = uR[i] - parameters["rectified_cx"] 
        vcR[i] = vR[i] - parameters["rectified_cy"] 
    
        d[i] = ucL[i] - ucR[i]
        d[i] = np.abs(d[i])
        Z[i] = parameters["rectified_fx"] * (parameters["baseline"] / d[i])  #  f * B / d 
        X[i] = ucL[i] * Z[i] / parameters["rectified_fx"]
        Y[i] = vcL[i] * Z[i] / parameters["rectified_fy"]
    
        print("X, Y, Z = {:.5f} {:.5f} {:.5f}".format(X[i], Y[i], Z[i]))
    
    return X[i], Y[i], Z[i]

#global X, Y, Z

##WRITE IN CODE FOR PARAMETERS
"""parameters_data = parameters.load_parameters("/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt")
for i in range(30):
    uL[i], uR[i], vL[i], vR[i] = parameters.get_coordinates()

    X[i], Y[i], Z[i] = calculate_coordinates(uL[i], uR[i], vL[i], vR[i], parameters_data)"""
