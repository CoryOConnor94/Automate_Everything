import cv2

video = cv2.VideoCapture('video.mp4')

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
num_of_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
print(f'Width = {width}, Height = {height}, '
      f'Number of frames = {num_of_frames}, Frames per second = {fps}')