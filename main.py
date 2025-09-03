import time
from operator import ifloordiv
import glob;
from emailing import send_email
import cv2

# Start video camera
video = cv2.VideoCapture(0);
time.sleep(1);

first_frame =  None;
status_list = [];
count=1;

while True:
    status = 0;
    # Read current frame from camera
    check, frame = video.read();

    # Convert frame to gray
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    # Clean frame from other details
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21,21), 0);

    # If is the first frame i get like font
    if first_frame is None:
        first_frame = gray_frame_gau;

    # fine diferent between first frame and current frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau);

    # Picxels separate
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1];

    # Dilation, extend white point to clean view
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2);

    # find conturs of object
    conturs, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

    for contur in conturs:
        # Ignore smole conturs
        if cv2.contourArea(contur) < 5000:
            continue;

        #Get sizes on rectangle out of conturs
        x, y, w, h = cv2.boundingRect(contur);
        # Paint rectangle with green
        reactangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3);
        if reactangle.any():
            status = 1;

            # Save frame like images
            cv2.imwrite(f"images/{count}.png", frame);
            count = count + 1;

            all_images = glob.glob("images/*.png");
            # Take middle image
            index = int(len(all_images) / 2);
            image_with_object = all_images[index];
            
    # fill status list array
    status_list.append(status);
    status_list = status_list[-2];

    #if first 1 second 0 object are leave
    if status_list[0] == 1 and status_list[1] == 0:
        send_email();

    cv2.imshow("My video", frame);
    # CReating key object
    key = cv2.waitKey(1);

    if key == ord('q'):
        break;

video.release();


