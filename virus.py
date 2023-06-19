import subprocess
import importlib

# Install opencv-python
try:
    importlib.import_module('cv2')
except ImportError:
    subprocess.check_call(['pip', 'install', 'opencv-python'])

import cv2

# Create the video capture object
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Read the first frame
ret, frame = cap.read()

# Create the pyramid lists for upscaling and downscaling
upscaled_pyramid = [frame]
downscaled_pyramid = [frame]
current_frame = frame

# Create windows to display the frames
cv2.namedWindow('Original Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Frame', 400, 400)

while True:
    # Upscale the current frame
    upscaled_frame = cv2.pyrUp(current_frame)

    # Add the upscaled frame to the upscaling pyramid list
    upscaled_pyramid.append(upscaled_frame)

    # Display the upscaling pyramid levels
    for i, img in enumerate(upscaled_pyramid):
        cv2.imshow(f'Upscaled Level {i}', img)

    # Reduce the size of the current frame by half
    downscaled_frame = cv2.pyrDown(current_frame)

    # Add the downscaled frame to the downsizing pyramid list
    downscaled_pyramid.append(downscaled_frame)

    # Display the downsizing pyramid levels
    for i, img in enumerate(downscaled_pyramid):
        cv2.imshow(f'Downscaled Level {i}', img)

    # Display the original frame
    cv2.imshow('Original Frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == 113:
        break

    # Read the next frame
    ret, frame = cap.read()

    # Update the current frame to the next frame for the next iteration
    current_frame = frame

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
