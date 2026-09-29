import time
from datetime import datetime
from pathlib import Path
import cv2
from config import CAMERA_INDEX, UNKNOWN_DIR, UNKNOWN_SAVE_COOLDOWN_SECONDS
from database import init_database, mark_attendance
from recognizer import FaceEngine

def draw(frame,r):
    x,y,w,h=[int(v) for v in r['face'][:4]]; color=(40,200,40) if r['authorized'] else (40,40,230)
    label=f"{r['name']}  {r['score']:.2f}" if r['authorized'] else f"UNKNOWN  {r['score']:.2f}"
    cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
    cv2.putText(frame,label,(x,max(25,y-10)),cv2.FONT_HERSHEY_SIMPLEX,.62,color,2)

def main():
    init_database(); engine=FaceEngine(); n=engine.build()
    if not n: print('No usable reference faces found.'); return
    print(f'Loaded {n} authorized people. Press Q to quit.')
    cap=cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened(): print('Could not open webcam.'); return
    last_unknown=0
    while True:
        ok,frame=cap.read()
        if not ok: break
        for r in engine.recognize(frame):
            draw(frame,r)
            if r['authorized']:
                if mark_attendance(r['name'],r['person_id']): print(f"[ATTENDANCE] {r['name']} {datetime.now():%H:%M:%S}")
            elif time.time()-last_unknown>=UNKNOWN_SAVE_COOLDOWN_SECONDS:
                UNKNOWN_DIR.mkdir(exist_ok=True); fn=UNKNOWN_DIR/f"unknown_{datetime.now():%Y%m%d_%H%M%S}.jpg"; cv2.imwrite(str(fn),frame); last_unknown=time.time()
        cv2.putText(frame,'SMART FACE ATTENDANCE SYSTEM',(15,35),cv2.FONT_HERSHEY_SIMPLEX,.8,(255,255,255),2)
        cv2.putText(frame,'Q = Exit',(15,frame.shape[0]-15),cv2.FONT_HERSHEY_SIMPLEX,.55,(255,255,255),1)
        cv2.imshow('Smart Face Attendance System',frame)
        if cv2.waitKey(1)&0xFF==ord('q'): break
    cap.release(); cv2.destroyAllWindows()
if __name__=='__main__': main()
