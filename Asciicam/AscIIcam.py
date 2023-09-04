import cv2
import numpy as np
import sys

from curses import wrapper

capt = cv2.VideoCapture(0)
chars= ' .\'`^",:;Il!i><~+_-?][}{\\1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
scale =0.1

def redraw(l):
    f=[]
    for x in range(len(l)):
        r=[]
        for y in range(len(l[x])):
            p=[]
            p.append(l[x][y][0])
            p.append(l[x][y][0])
            p.append(l[x][y][0])
            r.append(p)
        f.append(r)

    return np.array(f, dtype= np.uint8)

def renderToscreen(charList,screen):
    for x,y in enumerate(charList):
        try:
            screen.addstr(x,0,y)
        except:
            pass
    screen.refresh()
    
    return

def pixelTochar(l):
    charL=[]
    for x,y in enumerate(l):
        row=""
        for i,j in enumerate(y):
            pixB=(int(j[0])+int(j[1])+int(j[2]))/3
            ind=(pixB/255)*len(chars)
            charvalue= chars[int(ind)]
            row+=charvalue
            row+=charvalue
        charL.append(row)
    








    return charL





def main(screen):
    screen.clear
    while True:
        ret, frame = capt.read()

        frame_resized = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

        charMat=pixelTochar(frame_resized)
        renderToscreen(charMat,screen)
        #cv2.imshow('Grayscale Webcam Feed', frame_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.out()
            break

    # Release the webcam and close all windows
    capt.release()
    cv2.destroyAllWindows()



wrapper(main)
