from pybullet_suite import *

world = BulletWorld(gui=True)
sm = BulletSceneMaker(world)
coord = sm.view_frame(Pose.identity(), "world", 0.5)
world.set_gravity([0,0,-9.8])

## object setting
ground = sm.create_plane()
#dual-arm
gap = 0.5
robot1 = world.load_robot(Panda, "robot1", Pose(trans=[0,gap/2,0]))
robot2 = world.load_robot(Panda, "robot2", Pose(trans=[0,-gap/2,0]))

robot1.set_ctrl_mode("torque")
robot2.set_ctrl_mode("torque")

while True:
    #control law
    robot1.set_joint_torques(np.zeros(7), gravity_comp=True)
    robot2.set_joint_torques(np.zeros(7), gravity_comp=True)
    world.step()