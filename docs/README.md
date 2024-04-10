Traffic Flow Optimization and Congestion Management

Problem: Evaluating the traffic congestion shown by map engine services against the calculated actual congestion using the Drone.

Solution: 
1. Detection of objects through the YOLO v8 model
2. Analyzing the coordinates of the drone
3. Detected videos to frames
4. Classification, validation, and severity analysis through the VGG16 model
5. Email alerts through SMTP protocols


Execution:
1. Clone the repo
2. Setting up the path - cd Traffic_Management_System
3. Install all the packages - pip install -r requirements.txt
4. By default the detected videos will be saved to the directory - Traffic_Management_System/runs/detect/predict{$number}
5. Go to Traffic_Management_System/runs - open VideoToImages.py file and change the path("video_path") of the detected video file [eg: predict which saves in increasing order (predict, predic2....)] and also the frames("output_folder") saving directory according to the local machine.
6. Go to predict.py in the main directory and change the path of the ("image_directory") same as the path of ("output_folder"), to the folder where the frames are located.


UNIX/LINUX machines:
1. If the local machine is "Unix/Linux" => ./Run.sh - run the bash file directly in the terminal

WINDOWS machines:
* Create a folder named "Pics" inside the runs/ folder => not preferable, as the folder will be generated automatically when the paths are set correctly.
1. If the local machine is "Windows" => Run.bat - run the bash file directly in the terminal or cmd.
2. If an error generates that the file Run.bat is not mentioned in environmental variables, copy the path of Run.bat file and add it to the path variables, exit the terminal or cmd, and re-run .Run.bat command.



**CHECK THE DIRECTORY PATHS** twice before executing the command irrespective of the local machines used.
**Recommendation**: Enter the full path of directories from the root drive/directory.
