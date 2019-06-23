import requests
import cv2
import base64

token = "YOUR_API_KEY"
toStore = str(0)
g_url = 'http://api.giscle.ml'

imageName = "/home/pranay/Desktop/mark.jpg"
img = open(imageName,'rb')
img = img.read()
image = base64.b64encode(img)
payload = {'image':image}

r = requests.post(g_url + ':80/image', files=payload, headers={'token':token,'store':toStore})

if r.ok:
    result = r.json()
    print(result)
    image = cv2.imread(imageName)
    for key in result['Data'][2].keys():
            x,y,h,w = result['Data'][2][str(key)]['rect_coordinate']
            cv2.rectangle(image, (x,y),(x+h,y+w), (255,255,255))
    cv2.imshow('Image',image)
    cv2.waitKey(0)
else:
    print(r.status_code)