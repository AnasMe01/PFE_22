import network, omv, rpc, sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)



omv.disable_fb(True)

interface = rpc.rpc_usb_vcp_slave()


def stream_generator_cb():
    return sensor.snapshot().compress(quality=90).bytearray()

def jpeg_image_stream_cb():
    interface.stream_writer(stream_generator_cb)


def jpeg_image_stream(data):
    pixformat, framesize = bytes(data).decode().split(",")
    sensor.set_pixformat(eval(pixformat))
    sensor.set_framesize(eval(framesize))
    interface.schedule_callback(jpeg_image_stream_cb)
    return bytes()

interface.register_callback(jpeg_image_stream)

interface.loop()