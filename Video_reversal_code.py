python -m pip install ffmpeg-python

import ffmpeg

input_video = 'video (2160p).mp4'
output_video = 'output.mp4'

# Reverse the video
reversed_video = ffmpeg.input(input_video).output('-', vf='reverse').run(capture_stdout=True, capture_stderr=True, input=None, quiet=True)

# Apply slow-motion effect (reduce speed by half)
slowed_video = ffmpeg.input('pipe:').output(output_video, r=30, vf='setpts=2.0*PTS').run(input=reversed_video.stdout, capture_stdout=True, capture_stderr=True, quiet=True)  # Remove input argument here

print('Video processing complete.')

