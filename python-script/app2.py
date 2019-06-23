import base64
import requests
import cv2
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InByYW5heWFnMTVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJwcmFuYXlhZzE1IiwiZmlyc3RuYW1lIjoiUHJhbmF5In0.8shWrxxBJjacd6s2mBRAHSolHXts06AoeqwnuCbomCo"
secret = "0804c167f81fa4366892abbb945b853e"

imgPath = '/home/pranay/Desktop/friends.jpg'

img = open(imgPath,'rb')
img = img.read()
# print (base64.b64encode('pranay',  'utf-8'))
img_enc = base64.b64encode(img)
img_enc = img_enc.decode('utf-8')

re = requests.post('http://api.giscle.ml/body_detection',data={'image':img_enc},headers={'token': token})

if re.ok:
    print(re.json())
    r = re.json()
    frame = cv2.imread(imgPath)
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
else: 
    print("hehhehh")