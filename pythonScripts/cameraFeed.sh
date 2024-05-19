#!/bin/bash

# Loop 5 times
for ((i = 1; i <= 5; i++)); do
    echo "Capturing video $i..."
    ffmpeg -f v4l2 -t 30 -framerate 25 -video_size 640x480 -i /dev/video0 output_$i.mp4  
    echo "Video $i captured."
done

echo "All videos captured successfully."