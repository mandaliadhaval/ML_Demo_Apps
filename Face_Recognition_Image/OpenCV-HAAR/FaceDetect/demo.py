# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:31:58 2017

@author: dhavalma
"""

import cv2
import sys

def run_training(imagePath):
    cascPath = "haarcascade_frontalface_default.xml"
    
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
    print("Found {0} faces!".format(len(faces)))
    print(faces)
    
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

    
    return image