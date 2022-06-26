from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
 
sleep(2)
camera.capture('test_photo.jpg')
#camera.capture('test_photo.jpg',resize=(320,240))

#camera.stop_preview()
#camera.close()