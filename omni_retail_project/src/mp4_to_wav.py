b

echo "ffmpeg -i ${f%%.*}.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 ${f%%.*}.wav";
