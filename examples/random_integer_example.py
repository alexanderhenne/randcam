from randcam import RandCam

with RandCam(0, True) as rc:
    print("seeding...")

    while True:
        result, random = rc.seed(4)
        if result:
            print("seeding done!")
            break
        else:
            print("could not seed")

    print("random number: %d" % random.randint(10, 50))
