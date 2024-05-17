# calculations.py

def calculate_coordinates(uL, uR, vL, vR, parameters):
    """
    Calculate 3D coordinates (X, Y, Z) from pixel coordinates and camera parameters.

    Args:
        uL (list): u-coordinates of the left image pixels.
        uR (list): u-coordinates of the right image pixels.
        vL (list): v-coordinates of the left image pixels.
        vR (list): v-coordinates of the right image pixels.
        parameters (dict): Camera calibration parameters.

    Returns:
        tuple: Tuple containing the lists of X, Y, and Z coordinates.
    """

    # Initialize empty lists to store the calculated coordinates
    X, Y, Z = [], [], []

    for i in range(30):
        # Calculate the coordinates of the current pixel in the left image
        ucL = uL[i] - parameters["rectified_cx"]
        vcL = vL[i] - parameters["rectified_cy"]
        # Calculate the coordinates of the corresponding pixel in the right image
        ucR = uR[i] - parameters["rectified_cx"]
        vcR = vR[i] - parameters["rectified_cy"]

        # Calculate the disparity between the left and right images
        d = abs(ucL - ucR)
        # If the disparity is zero, set it to 1 to avoid division by zero
        if d == 0:
            d = 1

        # Calculate the 3D coordinates of the current pixel
        Z_i = parameters["rectified_fx"] * (parameters["baseline"] / d)  # f * B / d
        X_i = ucL * Z_i / parameters["rectified_fx"]
        Y_i = vcL * Z_i / parameters["rectified_fy"]

        # Append the calculated coordinates to the respective lists
        X.append(X_i)
        Y.append(Y_i)
        Z.append(Z_i)

        # Print the calculated coordinates
        print(f"X, Y, Z = {X_i:.5f} {Y_i:.5f} {Z_i:.5f}")

    # Return the lists of X, Y, and Z coordinates
    return X, Y, Z

def display_points(X, Y, Z):
    """
    Display 3D points in a simple visualization.

    Args:
        X (list): List of X coordinates.
        Y (list): List of Y coordinates.
        Z (list): List of Z coordinates.
    """
    # Import the necessary module for 3D plotting
    import matplotlib.pyplot as plt

    # Create a new figure
    fig = plt.figure()
    # Create a 3D axes object
    ax = fig.add_subplot(111, projection='3d')
    # Scatter plot the 3D points
    ax.scatter(X, Y, Z, c='r', marker='o')
    # Set labels for the axes
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    # Show the plot
    plt.show()

