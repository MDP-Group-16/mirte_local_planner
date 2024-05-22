# turtle_dwa
A `turtlesim` environment to test the Dynamic Window Approach (DWA), a local planner for mobile robots, which is part of the ROS navigation stack. DWA will be used on the Mirthe Master robot as a local planner.

## Installation

First, ensure you have the ROS navigation stack installed. The navigation stack is split into several packages: `nav_core`, `move_base`, and `amcl`.

To create a new package with the necessary dependencies, use the following commands:

```bash
cd ~/catkin_ws/src
catkin_create_pkg turtle_dwa rospy std_msgs geometry_msgs nav_msgs turtlesim move_base
```

## Usage

### Start ROS Core

Before running any nodes, start the ROS core:

```bash
roscore
```

### Build and Source the Workspace

Navigate to your catkin workspace, build the workspace, and source the setup file:

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### Launch the Simulation

Launch the `turtle_dwa` simulation environment:

```bash
roslaunch turtle_dwa turtle_dwa.launch
```

For quick build, source and launch, you can also use the following command directly:

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch turtle_dwa turtle_dwa.launch
```

### Monitor via RViz
Load a Preconfigured RViz Setup:

```
rviz -d ~/catkin_ws/src/turtle_dwa/config/turtle_dwa.rviz
```

### Set a Goal for Turtle2

To set a goal for `turtle2`, publish a goal to the `/turtle2/move_base_simple/goal` topic. Here is an example command to set a goal at coordinates (9.0, 9.0):

```bash
rostopic pub /turtle2/move_base_simple/goal geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'world'
pose:
  position:
    x: 9.0
    y: 9.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
```

### Additional Notes

- Ensure that all necessary dependencies are installed and sourced properly.
- Use RViz to visualize the navigation and the costmap to debug and verify the robot's movement and obstacle avoidance.

By following these instructions, you should be able to set up and run the `turtle_dwa` simulation environment and test the DWA local planner with `turtlesim`. If you encounter any issues, make sure to check for error messages in the terminal and ensure all necessary ROS packages are correctly installed and sourced.
