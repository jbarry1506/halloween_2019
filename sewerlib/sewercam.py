
import time

# define function to control the camera
def cam_controller(cam, seen, dt, fl):
    if seen:
        cam.capture(fl+dt+".jpg")
        cam.start_recording(fl+dt+".h264")
        time.sleep(5)
        poll_cam = it_saw_you()
        if not poll_cam:
            cam.stop_recording()


def it_saw_you():
    pass