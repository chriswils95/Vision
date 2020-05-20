from jetcam.csi_camera import CSICamera
import cv2

camera = CSICamera(width=224, height=224, capture_width=1080, capture_height=720, capture_fps=30)

camera.read()

image = camera.value

#camera.running = True

cv2.imshow("image", image)

cv2.waitKey(5000)

#video = cv2.VideoCapture(0)

#check, frame = video.read()

#print(frame)


