# VIPS: Real-Time Perception Fusion for Infrastructure-Assisted Autonomous Driving

## Description

This project implements the [VIPS](https://yanzhenyu.com/assets/pdf/VIPS-MobiCom22.pdf) architecture from scratch. The implementation can be used for indenpendent research or benchmarking with other registration algorithms. This project was used to benchmark with [VI-Eye](https://dl.acm.org/doi/10.1145/3447993.3483276). 

## Getting Started

### Dependencies

* This implementation works on Linux, Windows and macOS. It requires Python 3.7+, CUDA 10.0+, and PyTorch 1.8+

### Installing
* First, we will clone the project. Since this project has two submodules, you also need to clone them into your machine too. 
```
git clone --recurse-submodules --remote-submodules https://github.com/btn6364/VIPS.git
```

* Create a Miniconda environment and activate it. If you don't know how to use Miniconda, an installation guide can be found [here](https://docs.anaconda.com/free/miniconda/). Run the following command to create a virtual environment, in this case I used Python 3.11. 
```
conda create -n vips python=3.11
conda activate vips
```

* Next, we will install MMDetection3D, a library for 3D object detection, a complete installation guide can be found [here](https://mmdetection3d.readthedocs.io/en/latest/get_started.html). 

* Install all the dependencies in `requirements.txt`
```
pip install -r requirements.txt
```

### Executing program
* VIPS pipeline has 4 components: 3D Object Detection, Frame Rectification, Co-visible Object Matching and Object Alignment. Due to the limited time, I decided to skip Frame Rectification. Future readers are free to implement this feature to increase the model's performance. 

#### 3D Object Detection
* I used PointPillars for the detection component, a state-of-art algorithm for 3D Object Detection. This model requires the data to be in the KITTI format (.bin). So first, we need to convert the .pcd point clouds to .bin files. 
* Navigate to the `main` folder
```
cd main
```
* Run the convertor script
```
python pcd_to_bin.py
```
* Once you have the binary point clouds, apply PointPillars inference to get 3D object detections. The results are saved in the `mmdetection3d/outputs` folder as JSON files. The results include object labels, confidence scores, bounding boxes and box type. 
```
python inference_pointpillars.py
```

#### Co-visible Object Matching

#### Object Alignment

## Authors

Contributors names and contact info
ex. Bao Nguyen [btn6364@rit.edu]