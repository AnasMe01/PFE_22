import image, math, pyb, sensor, struct, time
uart_baudrate = 9600
uart = pyb.UART(3, uart_baudrate, timeout_char =1)
clock = time.clock()

threshold_index = 0 # 0 for red, 1 for green, 2 for blue

thresholds = [(23, 48, -128, 74, -37, 66), # generic_red_thresholds
(30, 100, -64, -8, -32, 32), # generic_green_thresholds
(0, 30, 0, 64, -128, 0)] # generic_blue_thresholds

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking

while(True):
    clock.tick()
    start = pyb.millis()
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=100, area_threshold=100, merge=False):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        print(blob.cx(), blob.cy(), blob.w(),blob.h())
        uart.write("%d ; %d ; %d ; %d \r\n " % (blob.cx(), blob.cy(),blob.w(),blob.h()))
    print(clock.fps())
