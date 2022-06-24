import cv2, time, pandas
from datetime import datetime

first_frame = None
df = pandas.DataFrame(columns=["start", "end"])

video = cv2.VideoCapture(0)
time.sleep(2)

status_list = [None, None]
times = []
while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(gray, first_frame)

    threshold_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    cnts, dummy = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status =1
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
    status_list.append(status)

    if status_list[-1] ==1 and status_list[-2] ==0:
        times.append(datetime.now())
    if status_list[-1] ==0 and status_list[-2] ==1:
        times.append(datetime.now())

    cv2.imshow("gray", gray)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("threshold", threshold_frame)
    cv2.imshow("color", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        if status == 1:
            times.append(datetime.now())
        break
for i in range(0, len(times), 2):
    df = df.append({"start": times[i], "end": times[i+1]}, ignore_index=True)
video.release()
cv2.destroyAllWindows()
df.to_csv("Times.csv")
