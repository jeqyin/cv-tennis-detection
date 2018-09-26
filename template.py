import cv2
import sys

#This function detects tennisballs in a given frame
#return bool, mat
def detect_tennisballs(frame):
    #write code here


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