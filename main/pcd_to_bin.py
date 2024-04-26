import numpy as np
from pypcd4 import PointCloud
import open3d as o3d
import os 

def pcd_to_bin(pcd_file, tag):
    # Read the PCD file
    pcd = o3d.t.io.read_point_cloud(pcd_file)

    # Get the positions and intensities
    positions = pcd.point.positions
    intensities = pcd.point.intensities

    # Copy to a numpy array
    points = np.zeros([positions.shape[0], 4], dtype=np.float32)
    points[:, 0] = positions[:, 0].numpy()
    points[:, 1] = positions[:, 1].numpy()
    points[:, 2] = positions[:, 2].numpy()
    intensities_copy = intensities.numpy().astype(np.float32).reshape((positions.shape[0],))
    points[:, 3] = intensities_copy

    # Save the binary point cloud
    file_name = pcd_file.split("/")[-1][:-4]
    dest_file = f"evaluation/{tag}_bin/{file_name}.bin"
    print(f"Saving {dest_file}...")
    with open(dest_file, "wb") as f:
        f.write(points.tobytes())

def convertAll():
    vehicle_pcd_dir = "evaluation/Vehicle"
    infra_pcd_dir = "evaluation/Infrastructure"

    # Iterate over files in Vehicle_PCD
    for filename in os.listdir(vehicle_pcd_dir):
        f = os.path.join(vehicle_pcd_dir, filename)
        pcd_to_bin(f, "vehicle")
    
    # Iterate over files in Infra_PCD
    for filename in os.listdir(infra_pcd_dir):
        f = os.path.join(infra_pcd_dir, filename)
        pcd_to_bin(f, "infra")

if __name__=="__main__": 
    convertAll()
    # num_infra_pcds = len(os.listdir("evaluation/Infrastructure"))
    # num_infra_bins = len(os.listdir("evaluation/infra_bin"))
    # print(f"Num I_PCDs = {num_infra_pcds}, Num I_BINs = {num_infra_bins}")

    # num_vehicle_pcds = len(os.listdir("evaluation/Vehicle"))
    # num_vehicle_bins = len(os.listdir("evaluation/vehicle_bin"))
    # print(f"Num V_PCDs = {num_vehicle_pcds}, Num V_BINs = {num_vehicle_bins}")