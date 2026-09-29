from pathlib import Path
from urllib.request import Request, urlopen
MODELS = {
 'face_detection_yunet_2023mar.onnx':'https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx',
 'face_recognition_sface_2021dec.onnx':'https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx'
}
root=Path('models'); root.mkdir(exist_ok=True)
for name,url in MODELS.items():
    p=root/name
    if p.exists() and p.stat().st_size>100000:
        print('[OK]',p); continue
    print('[DOWNLOAD]',name)
    try:
        req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urlopen(req,timeout=90) as r, open(p,'wb') as f: f.write(r.read())
        print('[OK]',p)
    except Exception as e: print('[ERROR]',e)
