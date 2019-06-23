import base64
import requests
import cv2
import time
from socketIO_client import SocketIO, LoggingNamespace
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InByYW5heWFnMTVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJwcmFuYXlhZzE1IiwiZmlyc3RuYW1lIjoiUHJhbmF5In0.8shWrxxBJjacd6s2mBRAHSolHXts06AoeqwnuCbomCo'

g_url = 'http://api.giscle.ml'

frame = 0

def dataFunction(img_enc, frame1):
    print("sending request")
    re = requests.post('http://api.giscle.ml/body_detection',data={'image':img_enc},headers={'token': token})

    if re.ok:
        print(re.json())
        r = re.json()
        frame = frame1
        for key in r['data'].keys():
            if key != 'total_person':
                x,y,h,w = (r['data'][str(key)])
                x,y,h,w = int(x),int(y),int(h),int(w)
                cv2.rectangle(frame, (x,y),(x+h,y+w), (255,0,0))
        while True:
            frame = cv2.resize(frame, (900, 600))
            cv2.imshow("frame",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# SocketIO = socket.socket()    
def extract_data(args):
    print(time.time() - t)
    print(args)
    for key in args['Output'].keys():
        if key != 'total_person':
            x,y,h,w = (args['Output'][str(key)])
            x,y,h,w = int(x),int(y),int(h),int(w)
            cv2.rectangle(frame, (x,y),(x+h,y+w), (255,255,255))

    cv2.imshow("frame",frame)

socketio = SocketIO(g_url, 80, LoggingNamespace)
socketio.emit('authenticate', {'token': token})

cam = cv2.VideoCapture(0)

frame_count = 1

while True:
    print(123)
    global t
    t = time.time()
    cap= cv2.VideoCapture('http://93.87.72.254:8090/mjpg/video.mjpg')
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, (900, 600))
    cv2.imshow("frame",frame)
    encoded, buffer = cv2.imencode('.jpg', frame)
    encoded_frame = base64.b64encode(buffer)
    encoded_frame = encoded_frame.decode('utf-8')
    socketio.emit('body_detection', {'data': encoded_frame})
    # dataFunction(encoded_frame, frame)
    # socketio.on('response', extract_data(encoded_frame))
    socketio.wait(0.0001)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
