import cv2

# Open the webcam
vid = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not vid.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    t, v = vid.read()

    if not t:
        print("Error: Failed to read frame.")
        break
    
    # Convert to gray scale
    gray = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to the grayscale image
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to the original frame to smooth it
    color = cv2.bilateralFilter(v, 9, 300, 300)

    # Combine the edges and the smoothed image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Show the result
    cv2.imshow('Cartoonized Webcam', cartoon)

    # Wait for a key event; 25ms delay
    key = cv2.waitKey(1) & 0xFF

    # If the 'a' key is pressed, break the loop
    if key == ord('a'):
        print("Closing webcam feed...")
        break

# Release the webcam and close all windows
vid.release()
cv2.destroyAllWindows()
