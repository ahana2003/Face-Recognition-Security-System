import cv2
from pathlib import Path
from config import DATASET_DIR, DETECTOR_MODEL, RECOGNIZER_MODEL, MATCH_THRESHOLD

class FaceEngine:
    def __init__(self):
        if not Path(DETECTOR_MODEL).exists(): raise FileNotFoundError(f'Missing: {DETECTOR_MODEL}')
        if not Path(RECOGNIZER_MODEL).exists(): raise FileNotFoundError(f'Missing: {RECOGNIZER_MODEL}')
        self.detector=cv2.FaceDetectorYN.create(str(DETECTOR_MODEL),'',(320,320),0.6,0.3,5000)
        self.recognizer=cv2.FaceRecognizerSF.create(str(RECOGNIZER_MODEL),'')
        self.references=[]
    def detect(self,img):
        h,w=img.shape[:2]; self.detector.setInputSize((w,h)); _,faces=self.detector.detect(img); return [] if faces is None else list(faces)
    def feature(self,img,face): return self.recognizer.feature(self.recognizer.alignCrop(img,face))
    def build(self):
        self.references.clear()
        for folder in sorted(Path(DATASET_DIR).iterdir()):
            if not folder.is_dir(): continue
            name=folder.name; pid=''
            if (folder/'id.txt').exists(): pid=(folder/'id.txt').read_text(encoding='utf-8').strip()
            for p in sorted(folder.iterdir()):
                if p.suffix.lower() not in {'.jpg','.jpeg','.png'}: continue
                img=cv2.imread(str(p))
                if img is None: continue
                faces=self.detect(img)
                if not faces: continue
                face=max(faces,key=lambda x:float(x[2]*x[3]))
                self.references.append((name,pid,self.feature(img,face))); break
        return len(self.references)
    def recognize(self,frame):
        out=[]
        for face in self.detect(frame):
            feat=self.feature(frame,face); best_name='Unknown'; best_id=''; best=-1.0
            for name,pid,ref in self.references:
                score=float(self.recognizer.match(feat,ref,cv2.FaceRecognizerSF_FR_COSINE))
                if score>best: best=score; best_name=name; best_id=pid
            ok=best>=MATCH_THRESHOLD
            out.append({'face':face,'name':best_name if ok else 'Unknown','person_id':best_id if ok else '','score':best,'authorized':ok})
        return out
