import cv2

video = cv2.VideoCapture('video.mp4')


def extract_all_frames():
    success, frame = video.read()
    count = 1
    while success:
        cv2.imwrite(f'frames/{count}.jpg', frame)
        success, frame = video.read()
        count += 1


def main():
    extract_all_frames()


if __name__ == '__main__':
    main()
