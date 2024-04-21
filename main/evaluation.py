# TODO: Write some evalutation code here. 
# TODO: Calculate RTE, RRE, latency and IoU. 
import numpy as np 
from math import atan2, asin

def rte(t1, t2): 
    dist = np.linalg.norm(t1 - t2).round(2) 
    return dist

def rre(R_t, R_e): 
    # Calculate the rotation matrix
    R_t_inversed = np.linalg.inv(R_t)
    R = np.matmul(R_t_inversed, R_e)
    
    # Calculate the three Euler angles (Z-Y-X order)
    yaw = atan2(R[1,0], R[0,0])
    pitch = -asin(R[2,0])
    roll = atan2(R[2,1], R[2,2])
    
    # Calculate the L1 distance
    dist = np.sum(np.abs(np.array([yaw, pitch, roll]))).round(2)
    return dist

if __name__=="__main__": 
    # t1 = np.array([1,2,3])
    # t2 = np.array([1,1,1])
    # dist = rte(t1, t2)
    # print(f"Distance = {dist}")
    R_t = np.array([
        [0.94, 0, 0.34], 
        [0, 1, 0], 
        [-0.34, 0, 0.94]
    ])
    R_e = np.array([
        [-0.0004, -0.99, 0.000009], 
        [0.99, -0.0004, 0.0002],
        [-0.0002, 0.000001, 1]
    ])
    dist = rre(R_t, R_e)
    print(f"Angles = {dist}")