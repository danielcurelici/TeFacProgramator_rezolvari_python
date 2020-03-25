import cv2
import numpy as np

#img = cv2.imread("big.jpg", 0)
#print(img)
#cv2.imwrite("big_gray.jpg",img)
#cv2.imshow("Ce nume vrea eu", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def read_video(filename):
    cap = cv2.VideoCapture(filename)
    
    while(True):
        ret, frame = cap.read()
        
        b = frame.copy()
        b[:,:,0] = 0
        b[:,:,1] = 0
        
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        cv2.imshow("My video", b)
        
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
if __name__ == "__main__":
    read_video("total.mp4")