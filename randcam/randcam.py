import cv2
import hashlib
import random
import binascii
import math


class RandCam(object):

    def __init__(self, source, debug=False):
        self.feed = cv2.VideoCapture(source)
        self.debug = debug

    def __enter__(self):
        return self

    def seed(self, minimum_entropy=0):
        if minimum_entropy > 0:
            while True:
                result, image = self.feed.read()

                if not result:
                    if self.debug:
                        print("image could not be captured")
                    return False, None

                entropy = shannon_entropy(image.tobytes())
                if entropy >= minimum_entropy:
                    if self.debug:
                        print("good entropy found (%f)" % entropy)
                    break
                elif self.debug:
                    print("bad entropy found (%f), min is %f" % (entropy, minimum_entropy))
        else:
            result, image = self.feed.read()
            if not result and self.debug:
                print("image could not be captured")
                return False, None

        m = hashlib.sha256()
        m.update(image.tobytes())
        digest = m.digest()

        if self.debug:
            print("using digest: %s" % binascii.hexlify(digest).decode("utf-8"))

        return True, random.SystemRandom(digest)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.feed.release()


def shannon_entropy(byte_array):
    freq_list = []

    for b in range(256):
        ctr = 0
        for byte in byte_array:
            if byte == b:
                ctr += 1
        freq_list.append(float(ctr) / len(byte_array))

    ent = 0.0

    for freq in freq_list:
        if freq > 0:
            ent += freq * math.log(freq, 2)

    return abs(ent)
