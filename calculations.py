import math
import parameters as param # Import parameters.py file
#import stereovision as sv # Import stereo_vision.py file



parameters = param.load_parameters("/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt")
uL, uR, v = param.get_coordinates()


def calculate_coordinates(uL, uR, v, parameters):
    
    ucL = uL - parameters["rectified_cx"] 
    vcL = v - parameters["rectified_cy"] 
 
    ucR = uR - parameters["rectified_cx"] 
    vcR = v - parameters["rectified_cy"] 
    print(ucL, vcL, ucR, vcR)

    d = ucL - ucR
    print(d)
    Z = parameters["focal_length"] * (parameters["baseline"] / d) #  f * B / d 
    print(Z)

    X = ucL * Z / parameters["focal_length"]
    Y = vcL * Z / parameters["focal_length"]


    
    return X, Y, Z

