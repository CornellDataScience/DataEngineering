# GPU Usage Tutorial


## Colaboratory
Currently GPU resources are available only through [Google Colaboratory](https://colab.research.google.com) notebooks.  
Google allows the use of a Nvidia K80 card for up to 12 hours a day.

To access the GPU, you must take the following steps:
1. Access 'Notebook Settings' by selecting 'Edit -> Notebook settings' in the Colaboratory tool bar
2. In the 'Hardware Accelerator' combobox, select 'GPU'
3. Accept changes

To check that the GPU has been activated, run a code cell containing:
```
import tensorflow as tf
tf.test.gpu_device_name()
```
If everything is working, you should get the following output:
```
'/device:GPU:0'
```

To use GPU acceleration for packages other than TensorFlow, you will have to install the packages using Pip and Apt. For example, to use OpenCV, you will need to add a cell containing the following commands to the top of your notebook:
```
!apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python
import cv2
```

This cell will have to be run each time you disconnect from the VM. To view a list of install commands for other libraries (including Pytorch and Keras), please see the Colaboratory documentation [here](https://colab.research.google.com/notebook#fileId=/v2/external/notebooks/snippets/importing_libraries.ipynb).