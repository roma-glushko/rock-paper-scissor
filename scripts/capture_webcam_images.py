import cv2

device = cv2.CAP_OPENNI

cam = cv2.VideoCapture(0)

img_counter = 0

# References:
# https://github.com/kevinam99/capturing-images-from-webcam-using-opencv-python


while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (300, 300))

    cv2.imshow("Webcam Steam", frame)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k % 256 == 32:
        # SPACE pressed
        img_name = "data/webcam/scissors/img_{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)

        print("{} saved".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
