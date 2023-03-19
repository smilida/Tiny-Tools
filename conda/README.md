# Conda
## Create a package of the C++ source code using conda-build
Below is a simple C++ example consisting of two .cpp files. We will package this example into an executable installer using Conda. Follow the steps outlined below:
1. Create a folder named "hello_world" and create the following three files inside:
 - hello.cpp: a C++ source code file containing a main function and a simple output statement.
 - my_math.cpp: a C++ soure code file containing a simple addition function.
 - Makefile: a Makefile used to compile and build the installation package.
 - meta.yaml: a metadata file used to describe the Conda installation package.
2. Build the installation package in the conda environment with the following command:
```
conda build hello_world
```
3. After the build is successful, use the following commands to install and test the installation package:
```
conda install --use-local hello_world
hello
```
#### Tips
Make sure the network is stable!!!
#### Reference
[使用conda-build构建包并上传至anaconda.org](https://www.jianshu.com/p/0b737a1ae425)

## Useful
 - [resetting conda channel priorities](https://stackoverflow.com/questions/48547046/resetting-conda-channel-priorities)
 - [为Conda添加清华软件源](https://zhuanlan.zhihu.com/p/47663391), Notes: Tsinghua source may not be complete.
