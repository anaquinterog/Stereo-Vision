import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv

def display_points(X, Y, Z):
    """
    Display 30 points in 3D space.

    Args:
        X (list): List of X coordinates.
        Y (list): List of Y coordinates.
        Z (list): List of Z coordinates.
    """
    # Plot 3D points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each point
    for x, y, z in zip(X, Y, Z):
        ax.scatter(x, y, z, color='b')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title('3D Scatter Plot of 30 Points')
    plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
