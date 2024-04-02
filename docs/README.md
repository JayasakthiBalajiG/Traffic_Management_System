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
3. Install all the packages - pip install -r requirements.txt
4. By default the detected videos will be saved to the directory - Traffic_Management_System/runs/detect/predict{$number}
5. Go to Traffic_Management_System/runs - open VideoToImages.py file and change the path("video_path") of the detected video file and also the frames("output_folder") saving directory according to the local machine.
6. Go to predict.py in the main directory and change the path of the ("image_directory") same as the path of ("output_folder"), to the folder where the frames are located.
7. ./Run.sh - run the bash file directly in the terminal - if the local machine is "Unix/Linux". Run.bat - run the bash file directly in the terminal - if the local machine is "Windows"
