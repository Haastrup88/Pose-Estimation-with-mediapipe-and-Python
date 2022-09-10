import cv2
print(cv2.__version__)

class mpPose:
    import mediapipe as mp
    def __init__(self,tole1=.5,tole2=.5):
        self.pose=self.mp.solutions.pose.Pose(False,False,True,tole1,tole2)
        self.draw=self.mp.solutions.drawing_utils
    def marks(self,frame):
        landmark=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=self.pose.process(frameRGB)
        if result.pose_landmarks !=None:
            self.draw.draw_landmarks(frame,result.pose_landmarks,self.mp.solutions.pose.POSE_CONNECTIONS)
            for lm in result.pose_landmarks.landmark:
                landmark.append((int(lm.x*width),int(lm.y*height)))
                #print(landmark)

        return landmark

width=1280
height=720 

eyeRad=10
eyeColor=(255,0,0)
eyeThick=-1

noseRad=10
noseColor=(0,0,255)
noseThick=-1
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
myPose=mpPose()

while True:
    _,frame=cam.read()
    poseData=myPose.marks(frame)
    cv2.circle(frame,poseData[2],eyeRad,eyeColor,eyeThick)
    cv2.circle(frame,poseData[5],eyeRad,eyeColor,eyeThick)
    cv2.circle(frame,poseData[0],noseRad,noseColor,noseThick)
    cv2.imshow("Windows",frame)
    cv2.moveWindow("Windows",0,0)
    if cv2.waitKey(1) & 0xff==ord("r"):
        break
cam.release()
