import cv2
import spoofed as sp
import os
import numpy as np
from pathlib import Path

detect = 0


def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1, y1 = pt1
    x2, y2 = pt2

    # Top left drawing
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right drawing
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left drawing
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right drawing
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)


def image_capture():
    global detect
    face_cascade = cv2.CascadeClassifier(
        "haarcascades/haarcascade_frontalface_default.xml"
    )
    
    # home would contain something like "/Users/jame"
    home = str(Path.home())

    path = home + "\Downloads\pic.jpg"
    image=cv2.imread(path)
    #image = cv2.imread(r"C:\\Users\\anica\\Downloads\\pic.jpg")
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    detect = len(faces)
        # print(detect)
    for x, y, width, height in faces:
        draw_border(
            image, (x, y), (x + width, y + height), (162, 255, 0), 2, 10, 10
        )
        cv2.putText(
            image,
            "face",
            (x, y - 4),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (192, 168, 0),
            2,
            cv2.LINE_AA,
        )
    cv2.imshow("image", image)
    return image


def result():
    image=image_capture()
    if detect == 1:
        # image = "download.jpeg"
        path = "./resources/anti_spoof_models"
        return sp.test(image, path, 0)
    else:
        return ("Face Not Detected")

# image = "./input/Fake_Faces/"
# i = 1
# for image_path in os.listdir(image):
#     # print(str(image_path))
#     image_path = os.path.join(image, image_path)
#     print(i)
#     path = "./resources/anti_spoof_models"
#     sp.test(image_path, path , 0)
#     i += 1
