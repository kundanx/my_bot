1. rviz2  := launch rviz
2. ros2 launch my_bot launch_sim.launch.py world:=./src/my_bot/worlds/my_world.world 
3.  ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/my_bot/config/mapper_params_online_async.yaml use_sim_time:=true 
4. ros2 launch my_bot navigation_launch.py map:=./my_map_save.yaml use_sim_time:=true



