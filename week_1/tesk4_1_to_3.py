# Cite reference
# Changing colorspaces. OpenCV. (n.d.). Retrieved October 4, 2022,
# from https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# OpenCV 프로젝트 : 8.5 - 객체 추적. 네이버 블로그 | 용쓰의 블로그. (n.d.)
# Retrieved October 4, 2022, from https://m.blog.naver.com/teach3450/221981892046

import numpy as np
import cv2


roi_hist = None  # Trace object histogram storage variable

win_name = 'Tracking'

termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cap = cv2.VideoCapture(0)

delay = int(1000 / 240)  # delay = 1000 / 240fps

while cap.isOpened():

    ret, frame = cap.read()

    img_draw = frame.copy()

    if roi_hist is not None:  # Tracked object histogram registered

        # whole image hsv color conversion

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Backprojection of full image histogram and roi histogram

        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ### Input, 1-channel, histogram to use for back-projection, ranges, scale

        # Track the average movement to the backprojection result and the initial tracking position

        ret, (x, y, w, h) = cv2.meanShift(dst, (x, y, w, h), termination)

        # show rectangle in new position

        cv2.rectangle(img_draw, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Combined color image and back-projection image

        result = np.hstack((img_draw, cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)))

    else:  # Tracked object histogram not registered

        cv2.putText(img_draw, 'Hit the Space and Drag and Hit again',

                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

        result = img_draw

    cv2.imshow(win_name, result)

    key = cv2.waitKey(delay) & 0xff

    if key == 27:  # ESC

        break

    elif key == ord(' '):  # Spacebar, set ROI

        x, y, w, h = cv2.selectROI(win_name, frame, False)

        if w and h:  # ROI set properly

            # Set ROI as initial tracking target location

            roi = frame[y:y + h, x:x + w]

            # change roi to HSV color

            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            mask = None

            # Calculate histogram for roi

            roi_hist = cv2.calcHist([roi], [0], mask, [180], [0, 180])

            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        else:  # ROI not set

            roi_hist = None

cap.release()

cv2.destroyWindow()