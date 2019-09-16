# Grace Hopper 2019 Hackathon on IoT & Analytics presented by Cisco #

## Machine Learning is Liberating ##

### Introduction ###
With over 35 years of networking expertise, Cisco has deployed more than 50 million networks in the past 20 years. Intent-based networking is providing easier operations for today’s complex, software-defined networks. But, as these networks grow increasingly larger, the vast programmability of devices and flexibility in their configuration leads to unimaginable levels of complexity. A network analytics engine, driven by Artificial Intelligence and Machine Learning (AI/ML), is simply the only way for humans to navigate this complexity. Similarly, to extract business value from the data generted by the billions of IoT devices, AI/ML, particularly AI/ML running at the edge close to devices, is going to serve as an importan tool.

### The Challenge ###
We have provided a [safety training video](https://www.youtube.com/watch?v=_o0T9G40Ehc) that was downloaded from the United States Department of Labor's YouTube channel. The video depicts an animated truck hitting an animated human. Your tasks involve using machine learning to detect scenarios where the human is in danger. The participants can then imagine that given more resources and more time, a system that keeps workers safe in the real world can be built.

#### Challenge 1 ####
Produce a video with bounding boxes around the objects of interest (`truck` and `person`). You can use any algorithm you want. But if you choose to, you are welcome to use [YOLO v3](https://pjreddie.com/darknet/yolo/) object detection algorithm and use the YOLO v3 weights that have been proivded [here](https://www.dropbox.com/s/b1x09r9hp9z7kap/osha.weights?dl=0).

#### Challenge 2 ####
To the video you produced for Challenge 1, overlay an alert if the truck too close to a person.

#### Challenge 3 ####
Train your own model, generate your own weights and redo Challenge 1 and Challenge 2.

#### Input (for all challenges) ####
* [`osha.mp4`](https://github.com/chelseacc/cisco-ghc-hackathon/blob/master/dataset/video/osha.mp4): Safety training video.
  * We have split the video into frames and these frames are in the [`dataset/images`](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/dataset/images) directory.
  * You are welcome to use these images as your imput for Challenge 1 and Challenge 2.
  * Note that for Challenge 3, you have to use these images so the bounding boxes from your solution can be checked and evaluated against our solution.

#### Output ####
* Reproduced Safety Training Video with bounding boxes around objects of interest and an alert when the human is in danger because of a potential truck back-over.
  * Please see our sample output in the [`sample_solution`](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/sample_solution) directory.

#### Submission ####
* A zip file with the following:
  * Your reproduced video from Challenge 2 in `.mp4` format
  * Your reproduced video from Challenge 3 in `.mp4` format 
  * For Challenge 3, in addition to the video, please provide bounding boxes for every frame in the [dataset](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/dataset/images) in JSON format.
    * Please see an example shown in [`sample_bounding_boxes.json`](https://github.com/chelseacc/cisco-ghc-hackathon/blob/master/sample_solution/sample_bounding_boxes.json) on how to format your JSON output.

#### Scoring ####
Your score will be based on [Intersection over Union metric.](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)

## Prerequisites ##
* [Python](https://www.python.org/downloads/)
* [Numpy](https://scipy.org/install.html)
* [Pytorch](https://pytorch.org/get-started/locally/)
* [OpenCV](https://pypi.org/project/opencv-python/)

## Getting Started ##

### Challenge 1 ###

We've provided 900 frames extracted from `osha.mp4` in `frames` to help you get started. In addition, we have provided selected [files](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/challenge1and2) from Andy Yun's [pytorch-0.4-yolov3 repo](https://github.com/andy-yun/pytorch-0.4-yolov3). This repo provides a Pytorch based implementation of the YOLO v3 object detection algorithm. This challenge can be solved by modifying detect.py.
* `detect.py`: YOLO v3 object detection algorithm
	* Dependencies (don't need to modify for this Challenge!):
		* `cfg.py`
		* `darknet.py`
		* `image.py`
		* `region_layer.py`
		* `utils.py`
		* `yolo_layer.py`
		* `osha.names`
* `yolo_v3.cfg`: config files for YOLO v3
* [`osha.weights`](https://www.dropbox.com/s/b1x09r9hp9z7kap/osha.weights?dl=0): weights from a model we've pretrained

### Challenge 2 ###

Read through `detect.py`'s dependency files -- see if you can figure out which function is responsible for drawing bounding boxes on the frames and how you can utilize that to overlay an alert when the truck is getting too close to the human

### Challenge 3 ###

In addition to the images in [dataset/images](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/dataset/images), use these file in the [dataset/labels](https://github.com/chelseacc/cisco-ghc-hackathon/tree/master/dataset/labels) directory:
* `osha_train.txt`: a text file with training data file names
* `osha_valid.txt`: a text file with validation data file names
* `lables.json`: a JSON file containing object ids and box coordinates
* `osha.names`: a text file containing id to object name mapping

## Resources ##
* [ffmpeg](https://ffmpeg.org/)
* Andy Yun's [pytorch-0.4-yolov3 repo](https://github.com/andy-yun/pytorch-0.4-yolov3)
* [YOLO](https://pjreddie.com/darknet/yolo/)



