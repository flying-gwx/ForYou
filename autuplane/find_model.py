# --coding:utf-8--


from math import sin,cos,radians,fabs
import copy
import time
import numpy as np
import cv2

def prethreatment(gray):
    thre = cv2.Canny(gray,100,100)
    # cv2.imshow("2",thre)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.dilate(thre,kernel)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(erosion,kernel)
    # k=np.ones((5,5),np.uint8)
    # erosion=cv2.morphologyEx(erosion,cv2.MORPH_CLOSE,k)
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(erosion,kernel)
    #erode

    #findContours
    contours,hier=cv2.findContours(erosion,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    return contours,gray

def pick_rectangels(contours):
    #choosecontours
    rec = []
    for c in contours:
        rect=cv2.minAreaRect(c)#计算出一个简单地边界框
        ((x,y),(w,h),r) = rect
        if (abs(w-h)<10) & (100>w>35):
            print(w,h)
            rec.append(((x,y),(w,h),r))
    return rec

def crop_minAreaRect(img_box, rect):
    mult = 1.2
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    W = rect[1][0]
    H = rect[1][1]
    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    rotated = False
    angle = rect[2]
    if angle < -45:
        angle+=90
    rotated = True
    center = (int((x1+x2)/2), int((y1+y2)/2))
    size = (int(mult*(x2-x1)),int(mult*(y2-y1)))
    # M = cv2.getRotationMatrix2D((size[0]/2, size[1]/2), angle, 1.0)
    cropped = cv2.getRectSubPix(img_box, size, center)
    # cropped = cv2.warpAffine(cropped, M, size)
    # croppedW = W if not rotated else H
    # croppedH = H if not rotated else W
    # croppedRotated = cv2.getRectSubPix(cropped, (int(croppedW*mult), int(croppedH*mult)), (size[0]/2, size[1]/2))
    return cropped

def decode_qrcodes(rec,gray):
    for index,r in enumerate(rec):
        center,(x,y),_ = r
        
        img = cv2.getRectSubPix(gray, tuple(map(int, ((x+10)*1.2,(y+10)*1.2))), tuple(map(int, center)))
        # img = crop_minAreaRect(gray.copy(), r)
        h,w = img.shape
        img = cv2.resize(img,(w*2,h*2))
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        detector = cv2.wechat_qrcode_WeChatQRCode()
        code, _ = detector.detectAndDecode(img)
        if code:
            print("wechart",code)


# 初始化摄像头




frame = cv2.imread('test.jpg',0)

    # w,h,_ = frame.shape
    # frame = frame[200:480,180:460]
    # w,h,_ = frame.shape
    
    # frame = cv2.resize(frame,(h*2,w*2))



contours,gray = prethreatment(frame)
rec = pick_rectangels(contours)

decode_qrcodes(rec,frame)

