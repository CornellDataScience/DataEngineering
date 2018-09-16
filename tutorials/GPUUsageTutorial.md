# GPU Usage Tutorial

## Why use a GPU?
GPUs are specialized processors. Like CPUs, they can execute instructions that are given to them by your code. However, [unlike CPUs](https://superuser.com/questions/308771/why-are-we-still-using-cpus-instead-of-gpus) they are designed to operate in a highly parallel fashion, with thousands of cores instead of 2-64 that may be found in modern CPUs (the GPU server's CPU has 32 cores, but even then its usually faster to train on the GPU!). The reason why parallelism is so important is because neural networks consist mostly of matrix multiplications. If you multiply two big matrices together, that is hundreds or thousands of numbers that all have to get multiplied and added up. Each core can do only one basic operation at a time, so if you have a lot of them you can perform the matrix multiplication faster. This is why specialized hardware like GPUs are so important.

The good news is that because video games are so popular and also rely on things like accelerated matrix arithmetic done in parallel, there are consumer level GPUs widely available that we can use. These consumer grade GPUs are [often faster than](https://medium.com/initialized-capital/benchmarking-tensorflow-performance-and-cost-across-different-gpu-options-69bd85fe5d58) the $10,000 plus GPUs used in data centers, because of the benefits of single or half precision over the double precision usually used in scientific computing, as well as circumventing the absurd markups that companies have to pay for things like error correcting computation and guarantees of stability. You can learn more about all the different sorts of hardware for deep learning [here](https://blog.inten.to/hardware-for-deep-learning-current-state-and-trends-51c01ebbb6dc).

## GPUs you can use
### The GPU server
CDS currently has one GPU server, that has space for up to 4 GPUs. Right now, we have one installed, with plans for more in the future. To connect to the server, read the [server tutorial](../ServerLoginTutorial.md). There are a bunch of additional libraries you would normall need to install to get GPU support working, but we have already [done that](https://www.tensorflow.org/install/install_linux#NVIDIARequirements) on the server. Once you SSH in, you should install the `tensorflow-gpu` package using pip or conda. Simply running `conda install tensorflow-gpu` or `pip install tensorflow-gpu` should work. Note that installing `tensorflow` instead of `tensorflow-gpu` will install tensorflow for the CPU instead of the GPU. Run `conda list` or `pip list` and make sure its listed in your package list.  We recommend installing the CPU version on laptops to allow you to develop your code and check if it runs, but do any serious training on the server with the GPU version.

### Colaboratory
An easy way to get a free but terrible gpu is through [Google Colaboratory](https://colab.research.google.com) notebooks.  
Google allows the use of a Nvidia K80 card for up to 12 hours a day.

To access the GPU, you must take the following steps:
1. Access 'Notebook Settings' by selecting 'Edit -> Notebook settings' in the Colaboratory tool bar
2. In the 'Hardware Accelerator' combobox, select 'GPU'
3. Accept changes

## Checking to make sure the GPU works
To check that the GPU has been activated, run a code cell containing:
```
import tensorflow as tf
sess = tf.InteractiveSession()
hi = tf.constant('Hello World!')
print(hi.eval())
print(tf.test.gpu_device_name())
```
If everything is working, you should get the following output:
```
Hello World!
/device:GPU:0
```
You can ignore warnings (Usually error messages prefixed with "W"), but errors are an issue (usually prefixed with "E").
