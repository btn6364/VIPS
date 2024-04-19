import numpy as np
from pypcd4 import PointCloud
import os

def pcd_to_bin(source_file, dataset, subdataset, filename, prefix):
    pcd_data = PointCloud.from_path(source_file)
    points = np.zeros([pcd_data.metadata.width, 4], dtype=np.float32)
    points[:, 0] = pcd_data.pc_data['x'].copy()
    points[:, 1] = pcd_data.pc_data['y'].copy()
    points[:, 2] = pcd_data.pc_data['z'].copy()
    points[:, 3] = pcd_data.pc_data['intensities'].copy().astype(np.float32)
    
    # Change .pcd file to .bin file
    dest_filename = filename[:-4] + ".bin"
    dest_file = f"../datasets/carla/{dataset}/{subdataset}/{prefix}_bin/{dest_filename}"
    print(f"Saving {dest_file}")
    with open(dest_file, 'wb') as f:
        f.write(points.tobytes())

def main():
    # datasets = ["Dataset_1", "Dataset_2", "Dataset_3"]
    datasets = ["Dataset_1"]
    # subdatasets = ["D1", "D2", "D3", "D4", "D5"]
    subdatasets = ["D1"]
    for dataset in datasets:
        for subdataset in subdatasets:
            vehicle_pcd_dir = f"../datasets/carla/{dataset}/{subdataset}/vehicle_pcd/"
            infra_pcd_dir = f"../datasets/carla/{dataset}/{subdataset}/infra_pcd/"
            # Iterate over files in Vehicle_PCD
            for filename in os.listdir(vehicle_pcd_dir):
                f = os.path.join(vehicle_pcd_dir, filename)
                pcd_to_bin(f, dataset, subdataset, filename, "vehicle")
            
            # Iterate over files in Infra_PCD
            for filename in os.listdir(infra_pcd_dir):
                f = os.path.join(infra_pcd_dir, filename)
                pcd_to_bin(f, dataset, subdataset, filename, "infra")

if __name__=="__main__":
    main()
    # num_vehicle_pcd = len(os.listdir("../datasets/carla/Dataset_1/D1/vehicle_pcd"))
    # num_vehicle_bin = len(os.listdir("../datasets/carla/Dataset_1/D1/vehicle_bin"))
    # print(f"Num V_PCD = {num_vehicle_pcd}, V_BIN = {num_vehicle_bin}")

    # num_infra_pcd = len(os.listdir("../datasets/carla/Dataset_1/D1/infra_pcd"))
    # num_infra_bin = len(os.listdir("../datasets/carla/Dataset_1/D1/infra_bin"))
    # print(f"Num I_PCD = {num_infra_pcd}, I_BIN = {num_infra_bin}")