import cv2
import binascii
from randcam import RandCam

with RandCam(0, True) as rc:
    result, random = rc.seed()

    while True:
        result, image = rc.feed.read()
        cv2.imshow('Captured Image', image)

        key = cv2.waitKey(1)
        # 'S' key - reseed
        if key == ord('s'):
            result, random = rc.seed()
        # 'R' key - print random string
        elif key == ord('r'):
            byte_array = bytearray(random.getrandbits(8) for i in range(32))
            print("random string: %s" % binascii.hexlify(byte_array).decode("utf-8"))
