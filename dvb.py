import time
import cv2

def image_proc():
    img = cv2.imread("C:/Users/Acer/Downloads/img_test.jpg")
     #w, h = img.shape[:2]
    # (cX, cY) = (w // 2, h // 2)
    # M = cv2.getRotationMatrix20((cX, cY), 45, 1.0)
   #  rotated = cv2.warpAffine(img, M, (w, h))
    #cv2.imshow("image", rotated)

    cat = img[250:580, 20:280]
    cv2.line(img, (0, 0), (580, 600), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 10), (510, 128), (0, 255, 0), 2)

    cv2.imshow("image", img)

image_proc()

def video_proc():
    cap = cv2.VideoCapture("C:/Users/Acer/Downloads/sample.mp4")
    down_points = (640, 480)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

        countours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_NONE)
        if len(countours) > 0:
            c = max(countours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.putText(frame, "x: " + str(x + w//2) + " y: " + str(y + h//2),  (40,  50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 200, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("vid", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        time.sleep(0.1)
    cap.release()

video_proc()

cv2.waitKey(0)
cv2.destroyAllWindows()