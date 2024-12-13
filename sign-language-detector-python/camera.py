from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.start_preview()
time.sleep(5)
picam2.stop_preview()
