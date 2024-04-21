# TODO: Write some evalutation code here. 
# TODO: Calculate RTE, RRE, latency and IoU. 
import numpy as np 

def rte(t1, t2): 
    dist = np.linalg.norm(t1 - t2).round(2) 
    return dist

if __name__=="__main__": 
    t1 = np.array([1,2,3])
    t2 = np.array([1,1,1])
    dist = rte(t1, t2)
    print(f"Distance = {dist}")
