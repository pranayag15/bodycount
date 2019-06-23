from pymongo import MongoClient
from time import gmtime, strftime
import base64
import requests
import cv2
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
client = MongoClient('mongodb://{0}:{1}@ds341847.mlab.com:41847/giscle'.format(os.getenv("DBUSERNAME"), os.getenv("PASSWORD")))
db=client.giscle

token = os.getenv("TOKEN")

frame = 0

def dataFunction(img_enc, iframe):
    print("sending request")
    re = requests.post('http://api.giscle.ml/body_detection',data={'image':img_enc},headers={'token': token})

    if re.ok:
        # print(re.json()["data"]['total_person'])
        r = re.json()
        print("body detected ", r["data"]["total_person"])
        frame = iframe
        for key in r['data'].keys():
            if key != 'total_person':
                x,y,h,w = (r['data'][str(key)])
                x,y,h,w = int(x),int(y),int(h),int(w)
                cv2.rectangle(frame, (x,y),(x+h,y+w), (255,0,0))
        while True:
            frame = cv2.resize(frame, (900, 600))
            cv2.imshow("frame",frame)
            print("here")
            detectedData = {
                'person_detected': r["data"]["total_person"],
                'time': strftime("%Y-%m-%d %H:%M:%S", gmtime())
            }
            result = db.person.insert_one(detectedData)
            print('Created {0} '.format(result.inserted_id))
            print("there")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            return

while (True):
    print(12345)
    cap= cv2.VideoCapture(os.getenv('CCTV'))
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, (900, 600))
    cv2.imshow("frame",frame)
    encoded, buffer = cv2.imencode('.jpg', frame)
    encoded_frame = base64.b64encode(buffer)
    encoded_frame = encoded_frame.decode('utf-8')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    dataFunction(encoded_frame, frame)
    print("back")