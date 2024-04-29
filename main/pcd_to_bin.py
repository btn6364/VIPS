import numpy as np
from pypcd4 import PointCloud
import open3d as o3d
import os 

def pcd_to_bin(pcd_file, tag):
    # Read the PCD file
    pcd = o3d.t.io.read_point_cloud(pcd_file)

    # Get the positions and intensities
    positions = pcd.point.positions

    # Copy to a numpy array
    points = np.zeros([positions.shape[0], 6], dtype=np.float32)
    points[:, 0] = positions[:, 0].numpy()
    points[:, 1] = positions[:, 1].numpy()
    points[:, 2] = positions[:, 2].numpy()

    # Copy intensities
    # intensities_copy = pcd.point.intensities.numpy().astype(np.float32).reshape((positions.shape[0],))

    # Copy object_tag, cosAngle and object_id 
    points[:, 3] = pcd.point.object_tag.numpy().astype(np.float32).reshape((positions.shape[0],))
    points[:, 4] = pcd.point.cosAngle.numpy().astype(np.float32).reshape((positions.shape[0],))
    points[:, 5] = pcd.point.object_id.numpy().astype(np.float32).reshape((positions.shape[0],))

    # Save the binary point cloud
    file_name = pcd_file.split("/")[-1][:-4]
    dest_file = f"../Segmentation_Dataset/{tag}_bin/{file_name}.bin"
    print(f"Saving {dest_file}...")
    with open(dest_file, "wb") as f:
        f.write(points.tobytes())

def convertAll():
    vehicle_pcd_dir = "../Segmentation_Dataset/Vehicle"
    infra_pcd_dir = "../Segmentation_Dataset/Infrastructure"

    # Iterate over files in Vehicle_PCD
    for filename in os.listdir(vehicle_pcd_dir):
        f = os.path.join(vehicle_pcd_dir, filename)
        pcd_to_bin(f, "vehicle")
    
    # Iterate over files in Infra_PCD
    for filename in os.listdir(infra_pcd_dir):
        f = os.path.join(infra_pcd_dir, filename)
        pcd_to_bin(f, "infra")

if __name__=="__main__": 
    # pcd_to_bin("../Segmentation_Dataset/Vehicle/0.pcd", "vehicle")
    convertAll()
    num_infra_pcds = len(os.listdir("../Segmentation_Dataset/Infrastructure"))
    num_infra_bins = len(os.listdir("../Segmentation_Dataset/infra_bin"))
    print(f"Num I_PCDs = {num_infra_pcds}, Num I_BINs = {num_infra_bins}")

    num_vehicle_pcds = len(os.listdir("../Segmentation_Dataset/Vehicle"))
    num_vehicle_bins = len(os.listdir("../Segmentation_Dataset/vehicle_bin"))
    print(f"Num V_PCDs = {num_vehicle_pcds}, Num V_BINs = {num_vehicle_bins}")