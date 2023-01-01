# R
Tips for using R
## 🔨Configure the R environment
1. Download and install Anaconda. Download Anaconda versions for different systems from [here](https://www.anaconda.com/products/distribution#Downloads).
Instructional video of anaconda installation [1](https://www.youtube.com/watch?v=AshsPB3KT-E) or
[2](http://lab.malab.cn/%7Etfr/Install_anaconda_in_Linux.mp4) (Copyright belongs to the original work).

2. Add channels to conda
```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

3. Create and Configure the R environment
```bash
# create a virtual environment called R(version=4.1)
conda create -n R r-base=4.1 r-essentials r-irkernel

# activate virtual environment R
conda activate R
```
4. Install devtools and 
```bash
conda install r-devtools
```
