# Robin
Robin is a programming language that can extract information from videos and store it in JSON string format.

### Why Robin?
Robots are capturing more information than ever. Particularly, new sensors are designed with integrated cameras that continously capture video of their environments. This means that there is a need to process that information in a way that takes very little storage, but at the same time, retains the crux of that information. Robin is, therefore, designed to process video data and output JSON strings that are light and meaningful.

### How to Use Robin?
Robin is currently in development. Till now, we have completed the following modules:

- Video Capturing: A robot can be interfaced with Robin through DataPreparation module which connects with the camera and stores information frame by frame.
- Object Mapping: The module detects all objects in a frame by first finding SURF Descriptors in the image and then clustering those descriptors. The output contains all sub-images that have one or more objects in them.
- Object Classification: The module classifies objects into human, animal or thing using machine learning techniques.
- JSON String Formation: The module forms JSON strings which are of the following format:


