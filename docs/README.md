Traffic Flow Optimization and Congestion Management

Problem: Evaluating the traffic congestion shown by map engine services against the calculated actual congestion using the Drone.

Solution: 
1. Detection of objects through YOLO v8 model
2. Analyzing the coordinates of the drone
3. Detected videos to frames
4. Classification, validation, and severity analysis through the VGG16 model
5. Email alerts through SMTP protocols


Execution:
1. Clone the repo
2. Setting up the path - cd Traffic_Management_System
3. By default the detected videos will be saved to the directory - Traffic_Management_System/runs/detect/predict{$number}
   Go to Traffic_Management_System/runs - open VideoToImages.py file and change the path of the detected video file and also the frames saving directory according to the local machine.
5. ./Run.sh - run the bash command directly in the terminal
