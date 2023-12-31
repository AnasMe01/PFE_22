import io, pygame, rpc, serial, serial.tools.list_ports, socket, sys


try: input = raw_input
except NameError: pass


print("\nAvailable Ports:\n")
for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))
sys.stdout.write("\nPlease enter a port name: ")
sys.stdout.flush()
interface = rpc.rpc_usb_vcp_master(port=input())
print("")
sys.stdout.flush()


pygame.init()
screen_w = 640
screen_h = 480
try:
    screen = pygame.display.set_mode((screen_w, screen_h), flags=pygame.RESIZABLE)
except TypeError:
    screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Frame Buffer")
clock = pygame.time.Clock()


def jpg_frame_buffer_cb(data):
    sys.stdout.flush()

    try:
        screen.blit(pygame.transform.scale(pygame.image.load(io.BytesIO(data), "jpg"), (screen_w, screen_h)), (0, 0))
        pygame.display.update()
        clock.tick()
    except pygame.error: pass

    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

while(True):
    sys.stdout.flush()

   
    result = interface.call("jpeg_image_stream", "sensor.RGB565,sensor.QQVGA")
    if result is not None:

        interface.stream_reader(jpg_frame_buffer_cb, queue_depth=8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()