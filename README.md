# 🛸 UFO-Detector - A simple UFO detection tool 🛸

 This is a project dedicated to using image recognition technology to create an internet-accessible program for classifying known and unknown objects within the view of a telescope.

[![GitHub issues](https://img.shields.io/github/issues/ZanzyTHEbar/UFO-Detector?style=plastic)](https://github.com/ZanzyTHEbar/UFO-Detector/issues) [![GitHub forks](https://img.shields.io/github/forks/ZanzyTHEbar/UFO-Detector?style=plastic)](https://github.com/ZanzyTHEbar/UFO-Detector/network) [![GitHub stars](https://img.shields.io/github/stars/ZanzyTHEbar/UFO-Detector?style=plastic)](https://github.com/ZanzyTHEbar/UFO-Detector/stargazers) [![GitHub license](https://img.shields.io/github/license/ZanzyTHEbar/UFO-Detector?style=plastic)](https://github.com/ZanzyTHEbar/UFO-Detector/blob/main/LICENSE)

Welcome to the **DIY UFO Detector**, automated *AI* and *Telescope* enabled :alien: .

## WHAT IS THIS PROJECT

With all of the hubub going on in the US, with ATIP, and the pentagon being forced to declassify documentation regarding un-identified flying objects - I have decided to build an open-source and automated classification system for a telescope and/or a lensed camera(s).

The idea of the project is to look to the skies and attempt to classify everything known to humans to fly in the sky (over a certain geo-specific area - this software uses geo-location to ensure performance on your machine, and to simplify the training).

The objects that are outside of the scope of the trained dataset are placed into a folder for further classification in order to weed out errors and smudges. The final filtered results are then left for human classification.

![Telescope with Camera]()

![AI Dataset Manipulation]()

![Software GUI]()

![Server Backend]()

### __*Development Steps*__

- [ ] Change source code to use FastAPI instead of Flask.  
- [ ] Create a GUI for the AI interface software.
- [ ] Port the GUI to a web-based interface.
- [ ] Gather all images from the sky using google images.
- [ ] Train our model using deep Learning Lobe.
- [ ] Deploy our model to the internet.
- [ ] Deploy to Raspberry Pi.
- [ ] Deploy to a mobile device.
- [ ] Integrate Smart Raspberrypi Telescope control and Stellarium Software interfacing.
- [ ] Integrate a web-based interface for the telescope.

## HOW TO SETUP

Setup is very straight forward, thankfully. You will need to purchase a few components before you begin:

__*Materials for purchase*__

1.
   1.
2.
3.

__*SETUP*__

1.
2.
3.
   1.
   2.

## HOW TO USE

Pre-trained models exist within the [/Models](https://github.com/ZanzyTHEbar/UFO-Detector/tree/main/UFO-Detector/model) folder

This project uses Lobe to generate the model, for this reason, it is recommended that you use the Lobe GUI to generate your model, should you wish to use a custom model. This is a free software, and can be found at: [Lobe](https://lobe.ai/)

Lobe is a free software utilized to expedite and automate the model training parameters.

This project utilises TensorFlow, and is compatible with most TensorFlow models, however it is optimized for Lobe generated models.

In-order to use this software, git clone this repo onto your desired server device. This server device **MUST** have at least one camera
connected to it.

```shell
git clone https://github.com/ZanzyTHEbar/UFO-Detector.git 
```

Once the software stack is installed, run the main.py file using

```shell

python3 main.py
```

After this, a locally hosted server instance will launch and can be accessed via your browser. In the browser, ensure to enable camera permissions and connect your cameras.

Ensure that a trained model (custom or built-in) is inside of the [/Models](https://github.com/ZanzyTHEbar/UFO-Detector/tree/main/UFO-Detector/model) folder.

## HOW TO SETUP REMOTE INSTANCE

Setup is very straight forward, thankfully. You will need to purchase a few components before you begin:

__*Materials for purchase*__

1.
   1.
2.
3.

__*SETUP*__

1.
2.
3.
   1.
   2.

## GOALS AND FUTURE FEATURES

1. Compatibility with all Tensor Flow Models
   1. TensorFlowLite support and a branch of the project for mobile
2. Full User interface for controlling a servo-enabled camera and or telescope

3.

## USEFUL LINKS

1. [Rotary Encoder and Stellarium Setup](https://www.instructables.com/Control-Your-Telescope-Using-Stellarium-Arduino/)
2. [OnStep](https://onstep.groups.io/g/main/wiki/3861)
