# Car and Person Detection Using Tensorflow and Keras
## Required Links
- Link to [dataset](https://evp-ml-data.s3.us-east-2.amazonaws.com/ml-interview/openimages-personcar/trainval.tar.gz).
- Link to [Tensorflow Object Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).
- Link to [ipynb file](https://github.com/RahulMeduri3/car_and_person_detection_TF/blob/main/Person_Car_Detection.ipynb).

## About the model
1. The model is custom trained to detect objects **Person & Car** in an image.
2. Libraries used - Tensorflow and Keras in Google Colab on TPU instance.
3. Model architecture considered - [SSD MobileNet V2 320x320](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md). To download click [here](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz).
  #### Steps involved in model training:
  1. Install Object Detection API and the reference doucment can be found [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/2.2.0/install.html).
  2. Clone models from the tensorflow [github repository](https://github.com/tensorflow/models).
  3. Download images and it's annotations.
  4. Convert JSON into CSV using this Python [Script](https://github.com/RahulMeduri3/car_and_person_detection_TF/blob/main/json_to_csv_converter.py).
  5. Split the dataset into train and test.
  6. Generate tfrecord for train and test from csv.
  7. Create label mapping file.
  8. Clone [SSD MobileNet V2 320x320](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) model and modify its pipeline.config file.
  9. Train the model and get the checkpoints.
  10. Export the trained model.
  11. Predict on test images.
  12. Calculate metrics.

## Primary Analysis
* The dataset contains a total of **2239** images of different sizes containing cars and persons.
* The dataset contains two folders **annotations** and **images**
* All the images are high quality images and hence no image enhancement is needed.
* The annotations for image are in [COCO dataset format](https://cocodataset.org/#format-data) a JSON.

## Assumptions
* All images should be annotated with atleast one class.
* Annotations in the annotations file are appropriate.

## Conclusion
* The model is predicting cars better than persons with an IOU of 0.7

## Recommendation
* Use pre-trained model and its weights than custom training as existing models have already built on COCO dataset which can detect person and car.
* Build other models like ResNet and choose the model based on the accuracy .
* Use GPU for model training as it reduces training time.
* Increase batchsize and number of steps.
