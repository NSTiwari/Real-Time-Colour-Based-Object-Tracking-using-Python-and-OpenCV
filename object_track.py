import cv2
import numpy as np


def main():
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)   # capture video from WebCam

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:

        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red colour
        low = np.array([140, 150, 0], np.uint8)
        high = np.array([180, 255, 255], np.uint8)

        # blue colour
        # low = np.array([100, 50, 50], np.uint8)
        # high = np.array([140, 255, 255], np.uint8)

        # green colour
        # low = np.array([40, 50, 50], np.uint8)
        # high = np.array([80, 255, 255], np.uint8)

        # yellow colour
        # low = np.array([10, 50, 50], np.uint8)
        # high = np.array([50, 255, 255], np.uint8)

        # orange colour
        # low = np.array([9, 50, 50], np.uint8)
        # high = np.array([29, 255, 255], np.uint8)

        image_mask=cv2.inRange(hsv,low,high)
        output = cv2.bitwise_and(frame, frame, mask=image_mask)

        cv2.imshow("Original WebCam Feed", frame)  # display LIVE original WebCam feed
        cv2.imshow("Image Mask", image_mask)       # display the masked image
        cv2.imshow("Colour Tracking", output)      # display extracted colour

        if cv2.waitKey(1) == 27:                   # press Esc key to close
            break

    cv2.destroyAllWindows()                        # clear all windows
    cap.release()                                  # release all variables


if __name__ == "__main__":
    main()
