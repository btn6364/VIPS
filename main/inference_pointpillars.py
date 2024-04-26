import os
import subprocess 
import time

def runPointpillarsOnePointCloud(input, prefix): 
    config = "../mmdetection3d/configs/pointpillars/pointpillars_hv_secfpn_8xb6-160e_kitti-3d-3class.py"
    checkpoint = "../mmdetection3d/checkpoints/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class_20220301_150306-37dc2420.pth"
    output_directory = f"../mmdetection3d/outputs/test/{prefix}"
    demo_file = "../mmdetection3d/demo/pcd_demo.py" 
    command = ["python", demo_file, input, config, checkpoint, "--out-dir", output_directory]

    # Run demo/pcd_demo.py using run()
    # python demo/pcd_demo.py 
    # ../datasets/carla/Dataset_1/D1/infra_bin/1689811023.137300000.bin 
    # configs/pointpillars/pointpillars_hv_secfpn_8xb6-160e_kitti-3d-3class.py 
    # checkpoints/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class_20220301_150306-37dc2420.pth 
    # --out-dir="outputs/infra"
    subprocess.run(command)
    

def runPointpillarsAll():
    # Start a timer
    start_time = time.time()

    vehicle_bin_dir = f"../evaluation/vehicle_bin/"
    infra_bin_dir = f"../evaluation/infra_bin/"

    # Iterate over files in Vehicle_BIN
    for filename in os.listdir(vehicle_bin_dir):
        f = os.path.join(vehicle_bin_dir, filename)
        runPointpillarsOnePointCloud(f, "vehicle")
    
    # Iterate over files in Infra_BIN
    for filename in os.listdir(infra_bin_dir):
        f = os.path.join(infra_bin_dir, filename)
        runPointpillarsOnePointCloud(f, "infra")

    # End the timer 
    end_time = time.time()

    # Calculate elapsed time 
    elapsed_time = round(end_time - start_time, 2) 
    print(f"Latency for 3D object detection = {elapsed_time}")

if __name__=="__main__": 
    runPointpillarsAll()
    # runPointpillarsOnePointCloud("../datasets/carla/Dataset_1/D1/infra_bin/1689811023.137300000.bin", "Dataset_1", "D1", "infra")

    # num_vehicle_pcd = len(os.listdir("../datasets/carla/Dataset_1/D1/vehicle_pcd"))
    # num_vehicle_predictions = len(os.listdir("../mmdetection3d/outputs/carla/Dataset_1/D1/vehicle/preds"))
    # print(f"Num V_PCD = {num_vehicle_pcd}, V_PRED = {num_vehicle_predictions}")

    # num_infra_pcd = len(os.listdir("../datasets/carla/Dataset_1/D1/infra_pcd"))
    # num_infra_predictions = len(os.listdir("../mmdetection3d/outputs/carla/Dataset_1/D1/infra/preds"))
    # print(f"Num I_PCD = {num_infra_pcd}, I_PRED = {num_infra_predictions}")
