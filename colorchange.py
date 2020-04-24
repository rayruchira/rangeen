#importing Modules

import cv2
import numpy as np

#Capturing Video through webcam.

g = input("For applying the filter, enter: FILTER\nFor finding RGB value of a point, enter: RGB ") 
if g=='FILTER':
    img = cv2.imread('newflag.png')



        #converting frame(img) from BGR (Blue-Green-Red) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        #defining the range of colours
    yellow_lower = np.array([22,54,252],np.uint8)
    yellow_upper = np.array([39,255,255],np.uint8)

    red_gu = np.array([7,255,255],np.uint8)
    red_gl = np.array([0,16,16],np.uint8)
    red_bu = np.array([179,255,255],np.uint8)
    red_bl = np.array([173,182,133],np.uint8)

    green_l= np.array([33,109,99],np.uint8)
    green_u = np.array([74,255,255],np.uint8)

    brown_l= np.array([10,77,66],np.uint8)
    brown_u = np.array([20,255,179],np.uint8)

    orange_l= np.array([9,58,235],np.uint8)
    orange_u = np.array([20,255,255],np.uint8)

        
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    redb = cv2.inRange(hsv,red_bl,red_bu)
    redg = cv2.inRange(hsv,red_gl,red_gu)
    green = cv2.inRange(hsv,green_l,green_u)
    brown = cv2.inRange(hsv,brown_l,brown_u)
    orange = cv2.inRange(hsv,orange_l,orange_u)
        #Morphological transformation, Dilation         
    kernal = np.ones((5 ,5), "uint8")

    blue=cv2.dilate(yellow, kernal)

    b1 = cv2.dilate(redb,kernal)
    b2 = cv2.dilate(green,kernal)
    b3 = cv2.dilate(brown, kernal)
    b4 = cv2.dilate(orange, kernal)

    res=cv2.bitwise_and(img, img, mask = yellow)



    res=cv2.bitwise_and(img, img, mask = redb)
    res=cv2.bitwise_and(img, img, mask = redg)
    res=cv2.bitwise_and(img, img, mask = green)
    res=cv2.bitwise_and(img, img, mask = brown)
    res=cv2.bitwise_and(img, img, mask = orange)
        #Tracking Colour (Yellow) 
    (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
             area = cv2.contourArea(contour)
             if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    
                    text = 'yellow'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(0,0,255),1,cv2.LINE_AA)
                    
                                 
                            
                                                            


              #tracking redb     
    (_,contours,hierarchy)=cv2.findContours(redb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    
                    text = 'red'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(255,0,0),1,cv2.LINE_AA)
                    roi=img[x:x+w, y:y+h]
                    for i in range (x,x+w):
                        for j in range (y,y+h):
                            color = img[j,i]
                            if (color[0]<=179 and color[1]<= 255 and color[2] <=255 and color[0]>=173 and color[1] >= 182 and color[2]>=133):
                                    color[2]= color[2]+40
                                    color[1]=color[1]-20 
                    


#tracking redg     
    (_,contours,hierarchy)=cv2.findContours(redg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    
                    text = 'red'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(255,0,0),1,cv2.LINE_AA)
                    roi=img[x:x+w, y:y+h]
                    for i in range (x,x+w):
                        for j in range (y,y+h):
                            color = img[j,i]
                            if (color[0]<=7 and color[1]<= 255 and color[2] <=255 and color[0]>=0 and color[1] >= 16 and color[2]>=16):
                                    color[2]= color[2]+40
                                    color[1]=color[1]-20
                    


#tracking green     
    (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
             area = cv2.contourArea(contour)
             if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                    
                    text = 'green'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(255,0,255),1,cv2.LINE_AA)

                     
                    roi=img[x:x+w, y:y+h]
                    for i in range (x,x+w):
                        for j in range (y,y+h):
                            color = img[j,i]
                            
                            if (color[0]<=74 and color[1]<= 255 and color[2] <=255 and color[0]>=33 and color[1] >= 109 and color[2]>=99):
                                 color[1]= color[1]+40
                    
                    
#tracking brown    
    (_,contours,hierarchy)=cv2.findContours(brown,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
                    
                    text = 'brown'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                    
#tracking orange
    (_,contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                        
                    x,y,w,h = cv2.boundingRect(contour)     
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                    
                    text = 'orange'
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,text,(x+10,y+10), font, 0.5,(255,255,0),1,cv2.LINE_AA)
                    roi=img[x:x+w, y:y+h]
                    for i in range (x,x+w):
                        for j in range (y,y+h):
                            color = img[j,i]
                            if (color[0]<=20 and color[1]<= 255 and color[2] <=255 and color[0]>=9 and color[1] >= 58 and color[2]>=235):
                                    color[2]= color[2]+60
                                    color[1]=color[1]-20 

    cv2.imshow("Color Tracking",img)
    img = cv2.flip(img,1)

    cv2.waitKey(0)
        
    cv2.destroyAllWindows()
       
        
        
elif g=='RGB':
    events = [i for i in dir(cv2) if 'EVENT' in i]
    
    def rgb_val(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            region = img[x:x+2, y:y+2]
            b, g, r = np.mean(region, axis=(0, 1))
        
            B=int(b)
            G=int(g)
            R=int(r)
            text = str(R) + ' ' + str(G) +' '+ str(B)
            if (B<=179 and G<= 255 and R <=255 and B>=173 and G >= 182 and R>=133):
                    text = 'red'
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,text,(x,y), font, 1,(255,255,255),2,cv2.LINE_AA)
        
    img = cv2.imread('splash.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',rgb_val)

    while(1):
        cv2.imshow('image',img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
