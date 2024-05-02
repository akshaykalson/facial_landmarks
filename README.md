Facial Landmark Detection
This project utilizes the dlib library for facial landmark detection, enabling users to detect and visualize facial landmarks in images.

Prerequisites
Before running the code, make sure you have the following installed:

Python 3.x
dlib library
scikit-image library (skimage)
You can install the required libraries using pip:
pip install dlib scikit-image
Additionally, download the pretrained shape predictor model from here and extract it to your project directory.

Usage:
To run the facial landmark detection code:

Clone this repository to your local machine.
Navigate to the project directory.
Ensure your image file is located in the project directory.
Run the following command:
python facial_landmark_detection.py

The code will detect faces in the image, draw bounding boxes around them, and overlay facial landmarks.
