# Cite reference
# gündüz, ayşe bilge. (2020, March 23). Finding dominant colour on an image.
# Medium. Retrieved October 4, 2022, from
# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# Admin. (2021, May 26). Python opencv tutorial to capture images from Webcam Full Project.
# Coding Shiksha. Retrieved October 4, 2022, from
# https://codingshiksha.com/tutorials/python-opencv-tutorial-to-capture-images-from-webcam-full-project/
# !!!!how to work  !!!!!!
#   hit the space when camera capture.
import cv2

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


cam = cv2.VideoCapture(0)



img_counter = 0

while True:
    ret, frame = cam.read()



    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Hit the Space to take picture", frame)



    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))


        img_name = "opencv_frame_{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        img = cv2.imread(img_name)


        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = img.reshape((img.shape[0] * img.shape[1], 3))  # represent as row*column,channel number
        clt = KMeans(n_clusters=3)  # cluster number
        clt.fit(img)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)

        plt.axis("off")
        plt.imshow(bar)



        plt.show()

        img_counter += 1


cam.release()

cv2.destroyAllWindows()

