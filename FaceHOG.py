import cv2
from matplotlib import pyplot as plt
from skimage import exposure
from skimage.feature import hog

#HOG is a method designed to detect faces

image = cv2.imread(r"C:\Users\aksha\OneDrive\Documents\Python Projects\PyCharm\FaceRecognition\portrait1.jpg")
#cv2.imshow('Window Title', image)
#above line to convert array into image and plot it

fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, channel_axis= -1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()