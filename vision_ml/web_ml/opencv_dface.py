from django.conf import settings
from imageai.Detection import ObjectDetection
import numpy as np
import cv2
import os
from datetime import datetime
from .models import ImageUploadModel

def opencv_detector(path):
    img = cv2.imread(path, 1)
    cv2.imwrite(path+'_org', img)

    if (1== 1):
        execution_path = os.getcwd()
        print(execution_path)
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=(path),output_image_path=(path))

        objstr =[]
        for eachObject in detections:
            objstr.append(eachObject["name"])
            print("------------------")
            print(ImageUploadModel.objList)
            print("------------------")
            print(eachObject["name"], " : ", eachObject["percentage_probability"])
        ImageUploadModel.objList = objstr

    else:
        print('someting error')
        print(path)


def opencv_dface_org(path):
    img = cv2.imread(path, 1)

    if (type(img) is np.ndarray):
        print(img.shape)

        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        face_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_eye.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imwrite(path, img)

    else:
        print('someting error')
        print(path)
