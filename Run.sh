yolo predict model=yolov8n.pt source='traffic_mumbai.mp4'

cd runs
python3 VideoToImages.py

cd Pics
find . -name ".DS_Store" -print -delete
find . -name '.DS_Store' -type f -delete

cd ../..
python3 predict.py
