import cv2 
from datetime import datetime
import argparse
import os

face_cascade = cv2.CascadeClassifier("/Users/zeddkhan/Desktop/Projects simple/Python1/haarcascade_car_default.xml")

video = cv2.VideoCapture('/Users/zeddkhan/Desktop/Projects simple/Python1/car1.mp4')

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            exact_time = datetime.now().strftime('%Y-%b-%d-%H-%S-%f')
            path = "/Users/zeddkhan/Desktop/Projects simple/Python1/detected pics"
            cv2.imwrite(os.path.join(path, "face detected" + str(exact_time) + ".jpg"), img)

        cv2.imshow("home surv", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            ap = argparse.ArgumentParser()
            ap.add_argument("-ext", "--extension", required=False, default='jpg')
            ap.add_argument("-o", "--output", required=False, default='output.mp4')
            args = vars(ap.parse_args())

            dir_path = '.'
            ext = args['extension']
            output = args['output']

            images = []
            for f in os.listdir(dir_path):
                if f.endswith(ext):
                    images.append(f)

            image_path = os.path.join(dir_path, images[0])
            frame = cv2.imread(image_path)
            height, width, channels = frame.shape

            out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), 5.0, (width, height))

            for image in images:
                image_path = os.path.join(dir_path, image)
                frame = cv2.imread(image_path)
                out.write(frame)

            break  

video.release()
cv2.destroyAllWindows()
