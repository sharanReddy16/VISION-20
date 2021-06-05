import numpy as np
import cv2
import serial as ser


cap = cv2.VideoCapture(0)
print("connection established")
while True:
    ret,img=cap.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask = mask2+mask1
    
    b_l=np.array([90,50,150],np.uint8)
    b_u=np.array([128,255,255],np.uint8)
    

    blue=cv2.inRange(hsv, b_l, b_u)
    
    enc = ['l','f','r']
    
    maxareas = []
    argument = np.empty(2, dtype=int)
    res=cv2.bitwise_and(img, img, mask = mask)
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    maxarea=0
    cx1=0
    cy1=0
    
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>maxarea:
            maxarea=area
            M1 = cv2.moments(cnt)
            cx1 = int(M1['m10']/M1['m00'])
            cy1 = int(M1['m01']/M1['m00'])
    print(cx1,cy1)
    if cx1<215:
        ser.write(b'enc[0]')
    elif cx1>430:
        ser.write(b'enc[2]')
    else:
        ser.write(b'enc[1]')
    
    contours , hierarchy = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    maxarea=0
    cx2=0
    cy2=0
    
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>maxarea:
            maxarea=area
            M2 = cv2.moments(cnt)
            cx2 = int(M2['m10']/M2['m00'])
            cy2 = int(M2['m01']/M2['m00'])
    print(cx2,cy2)
    if cx2<=320:
        ser.write(b'enc[2]')
    elif cx2>320:
        ser.write(b'enc[0]')
         

        
    cv2.imshow('img',img)
    cv2.imshow('thresh1',mask)
    cv2.imshow('blue',blue)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
  
