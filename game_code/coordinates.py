import ikpy
import numpy as np
from ikpy import plot_utils

target_vector = [ 0.1, -0.2, 0.1]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector

my_chain = ikpy.chain.Chain.from_urdf_file("poppy_torso.URDF")

print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))

real_frame  = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))