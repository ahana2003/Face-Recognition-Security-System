import sys
from pathlib import Path
import cv2
from config import DATASET_DIR
if len(sys.argv)<2: print('Usage: python register.py "Person_Name"'); raise SystemExit
name=' '.join(sys.argv[1:]).strip(); folder=Path(DATASET_DIR)/name; folder.mkdir(parents=True,exist_ok=True)
cap=cv2.VideoCapture(0); count=0
if not cap.isOpened(): print('Could not open webcam.'); raise SystemExit
print('SPACE=capture, Q=finish')
while count<5:
    ok,frame=cap.read()
    if not ok: break
    cv2.putText(frame,f'{name} | Photo {count+1}/5 | SPACE capture | Q quit',(15,35),cv2.FONT_HERSHEY_SIMPLEX,.55,(255,255,255),2)
    cv2.imshow('Register Person',frame); key=cv2.waitKey(1)&0xFF
    if key==ord('q'): break
    if key==32: count+=1; p=folder/f'image{count}.jpg'; cv2.imwrite(str(p),frame); print('Saved',p)
cap.release(); cv2.destroyAllWindows()
