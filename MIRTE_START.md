# Starting up Mirte Master
Mirte id:
```
mirte-87efdb
```

## Setup your own laptop
Do this in your own terminal:
```bash
export ROS_IP=192.168.224.YOUR_IP
export ROS_MASTER_URI=http://192.168.224.39:11311
```

## Connecting with Mirte
Connect to Mirte
```bash
ssh mirte@192.168.224.39  
```

Optional:
```
ssh-copy-id mirte@192.168.224.39
```

## Setup Mirte (Once)
Do these commands on Mirte ssh
```bash
sudo service mirte-ros stop
export ROS_IP=192.168.224.39
roslaunch mirte_bringup minimal_master.launch
```


## Essentials commands
```
sudo service mirte-ros start
sudo service mirte-ros stop
sudo service mirte-ros restart
```

  camera_reading:
    topic: /camera/color/image_raw

    laptop test: /webcam/image_raw

rostopics:
/arm/joint_states
/arm/position_trajectory_controller/command
/arm/position_trajectory_controller/follow_joint_trajectory/cancel
/arm/position_trajectory_controller/follow_joint_trajectory/feedback
/arm/position_trajectory_controller/follow_joint_trajectory/goal
/arm/position_trajectory_controller/follow_joint_trajectory/result
/arm/position_trajectory_controller/follow_joint_trajectory/status
/arm/position_trajectory_controller/state
/camera/color/camera_info
/camera/color/image_raw
/camera/depth/camera_info
/camera/depth/image_raw
/camera/depth/points
/camera/ir/camera_info
/camera/ir/image_raw
/mirte/distance/left_front
/mirte/distance/left_rear
/mirte/distance/right_front
/mirte/distance/right_rear
/mirte/encoder/left_front
/mirte/encoder/left_rear
/mirte/encoder/right_front
/mirte/encoder/right_rear
/mirte/encoder_speed/left_front
/mirte/encoder_speed/left_rear
/mirte/encoder_speed/right_front
/mirte/encoder_speed/right_rear
/mirte/left_front
/mirte/left_rear
/mirte/motor_left_front_speed
/mirte/motor_left_rear_speed
/mirte/motor_right_front_speed
/mirte/motor_right_rear_speed
/mirte/movement/imu
/mirte/power/power_watcher
/mirte/power/power_watcher/used
/mirte/right_front
/mirte/right_rear
/mirte/servos/servoElbow/position
/mirte/servos/servoGripper/position
/mirte/servos/servoRot/position
/mirte/servos/servoShoulder/position
/mirte/servos/servoWrist/position
/mobile_base_controller/cmd_vel
/mobile_base_controller/odom
/rosout
/rosout_agg
/scan
/tf
/tf_static
/webcam/camera_info
/webcam/image_raw
/webcam/image_raw/compressed
/webcam/image_raw/compressed/parameter_descriptions
/webcam/image_raw/compressed/parameter_updates
/webcam/image_raw/compressedDepth
/webcam/image_raw/compressedDepth/parameter_descriptions
/webcam/image_raw/compressedDepth/parameter_updates
/webcam/image_raw/theora
/webcam/image_raw/theora/parameter_descriptions
/webcam/image_raw/theora/parameter_updates
