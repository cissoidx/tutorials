Graphcore
---
## Simple MNIST training example

This example trains a simple 2-layer fully connected model on the MNIST numeral data set.

### File structure

* `mnist.py` The main Python script.
* `README.md` This file.

### How to use this demo

1) Prepare the TensorFlow environment.

   Install the Poplar SDK. Make sure to run the enable.sh script for Poplar and activate a Python virtualenv with the tensorflow-2 wheel from the Poplar SDK installed.

2) Train the graph.

       python mnist.py

### Extra information

### Model

By default, the demo runs a two layer fully connected model.

#### Options
There are no options for this script.
