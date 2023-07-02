import sensor, image, math, rcpRPI, struct

sensor.reset() 
sensor.set_pixformat(sensor.RGB565) 
sensor.set_framesize(sensor.QVGA) 
sensor.skip_frames(time = 2000) 

interface = rcpRPI.rcp_usb_vcp_slave() 
def ipeg_snapshot(data):
    sensor.set_pixformat(sensor.RGB565) 
    sensor.set_framesize(sensor.QVGA)
    return sensor_snapshot.compress(quality=90).bytearray()

interface.register_callback(jpeg_snapshot)

interface.loop()