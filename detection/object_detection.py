# detection/object_detection.py
import numpy as np
from ultralytics import YOLO
from rest_framework.response import Response
mymodel=YOLO("MODELS/yolov8n.pt")

# Implement object detection using a pre-trained model
def detect_objects(image):
    
    # Perform object detection here and return the results as a list of dictionaries
    result=mymodel.predict(image)
    cc_data=np.array(result[0].boxes.data)
    
    if len(cc_data) != 0:
            predictions = []
            xywh=np.array(result[0].boxes.xywh).astype("int32")
            
            for (_, _, w, h), (x1, y1,_,_,conf,clas) in zip(xywh,cc_data):
                prediction = [x1, y1, w, h, clas, conf]
                predictions.append(prediction)

            return predictions
    # msg="'No Predictions in image'"
    return {"msg":"No detection"}