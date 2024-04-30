# VIPS: Real-Time Perception Fusion for Infrastructure-Assisted Autonomous Driving

## Description

This project implements the [VIPS](https://yanzhenyu.com/assets/pdf/VIPS-MobiCom22.pdf) architecture from scratch. The implementation can be used for independent research or benchmarking with other registration algorithms. This project was used to benchmark with [VI-Eye](https://dl.acm.org/doi/10.1145/3447993.3483276). 

## Getting Started

### Dependencies

* This implementation works on Linux, Windows, and macOS. It requires Python 3.7+, CUDA 10.0+, and PyTorch 1.8+

### Installing
* First, we will clone the project. Since this project has two submodules, you also need to clone them into your machine. 
```
git clone --recurse-submodules --remote-submodules https://github.com/btn6364/VIPS.git
```

* Create a Miniconda environment and activate it. If you don't know how to use Miniconda, an installation guide can be found [here](https://docs.anaconda.com/free/miniconda/). Run the following command to create a virtual environment, in this case, I used Python 3.11. 
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
* VIPS pipeline has 4 components: 3D Object Detection, Frame Rectification, Co-visible Object Matching, and Object Alignment. Due to the limited time, I decided to skip Frame Rectification. Future readers are free to implement this feature to increase the model's performance. 

#### 3D Object Detection
* I used PointPillars for the detection component, a state-of-the-art algorithm for 3D Object Detection. This model requires the data to be in the KITTI format (.bin). So first, we need to convert the .pcd point clouds to .bin files. 
* Navigate to the `main` folder
```
cd main
```
* Run the converter script
```
python pcd_to_bin.py
```
* Once you have the binary point clouds, apply PointPillars inference to get 3D object detections. The results are saved in the `mmdetection3d/outputs` folder as JSON files. The results include object labels, confidence scores, bounding boxes, and box types. 
```
python inference_pointpillars.py
```

#### Co-visible Object Matching
* Once the infrastructure transfers the 3D object detection results to the vehicle, it's time to do object matching. First, navigate to the corresponding folder. 
```
cd VIPS_co_visible_object_matching/
```

Run the following command to get matching in a single point-cloud frame. The result is a list of tuples (i, j) where i is a detected object in the infrastructure frame while j is a detected object in the vehicle frame. 
```
python co_visible_object_matching.py 
```

#### Object Alignment
* Find the transformation matrix T that allows us to transform the detections from the infrastructure to the vehicle. Run the following command to get the transformation matrices for all point cloud frames.
```
python object_alignment.py 
```

### Evaluation 
* I implemented two evaluation metrics RRE and RTE. Run the following command to calculate the two metrics 
```
python evaluation.py
```

## Authors

Contributors names and contact info
ex. Bao Nguyen [btn6364@rit.edu]