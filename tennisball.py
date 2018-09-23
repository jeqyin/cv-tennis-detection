import cv2
import sys

def green_filter(frame):
    lowerBound = (26, 50, 150)
    upperBound = (60, 210, 255)

    mask = cv2.inRange(frame, lowerBound, upperBound)
    return mask


def detect_tennisballs(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = green_filter(hsv)
    mask = cv2.medianBlur(mask, 11)

    contours = [None] * 1
    image, contours, hierarchy = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    centers = [None] * len(contours)
    radius = [None] * len(contours)

    for i in range(len(contours)):
        contours[i] = cv2.approxPolyDP(contours[i], 3, True)
        centers[i], radius[i] = cv2.minEnclosingCircle(contours[i])

    for i in range(len(contours)):
        color = (0, 0, 255)
        cv2.drawContours(frame, contours, i, color, 1)
        rounded = (round(centers[i][0]), round(centers[i][1]))
        cv2.circle(frame, rounded, int(radius[i]), color, 2)

    if(len(contours) != 0):
        return True, frame
    return False, frame


def main():
    filename = sys.argv[1]
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    exists, result = detect_tennisballs(img)

    if exists:
        print("Tennis ball!!!")
    else:
        print("No tennis ball :(")
    cv2.imshow('image',result)
    cv2.waitKey(0)


    

if __name__ == "__main__":
    main()