@echo off

REM Predict using YOLOv8n model
yolo predict model=yolov8n.pt source='traffic_mumbai.mp4'

REM Change directory to 'runs'
cd runs

REM Execute VideoToImages.py script
python VideoToImages.py

REM Change directory to 'Pics'
cd Pics

REM Remove .DS_Store files
for /r %%i in (*.DS_Store) do (
    del "%%i"
)

REM Change directory back to the root directory
cd ..

REM Execute predict.py script
python predict.py 
