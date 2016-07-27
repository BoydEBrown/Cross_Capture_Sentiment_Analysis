'''
Convert current directory  *.mp4 files to *.wav
'''
#!/bin/bash

for f in *.mp4;
do
     echo "${f%%.*}";
     ffmpeg -i ${f%%.*}.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 ${f%%.*}.wav
done
