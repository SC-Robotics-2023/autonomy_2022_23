# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2021-2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Launch file to bring up visual slam node standalone."""
    visual_slam_node = ComposableNode(
        name='visual_slam_node',
        package='isaac_ros_visual_slam',
        plugin='isaac_ros::visual_slam::VisualSlamNode',
        remappings=[('/stereo_camera/left/camera_info', '/zed2i/zed_node/left/camera_info'),
                    ('/stereo_camera/right/camera_info', '/zed2i/zed_node/right/camera_info'),
                    ('/stereo_camera/left/image', '/zed2i/zed_node/left/image_rect_gray'),
                    ('/stereo_camera/right/image', '/zed2i/zed_node/right/image_rect_gray'),
                    ('visual_slam/imu', '/zed2i/zed_node/imu/data')],
        parameters=[{
                    'use_sim_time': False,
                    'denoise_input_images': True,
                    'rectified_images': True,
                    'enable_slam_visualization': False,
                    'enable_observations_view': False,
                    'enable_landmarks_view': False,
                    'enable_debug_mode': False,
                    'debug_dump_path': '/tmp/elbrus',
                    'map_frame': 'map',
                    'odom_frame': 'odom',
                    'base_frame': 'base_link',
                    'enable_imu': True,
                    'input_imu_frame': 'zed2i_imu_link',
                    'enable_localization_n_mapping': True,
                    'input_left_camera_frame': 'zed2i_left_camera_frame',
                    'input_right_camera_frame': 'zed2i_right_camera_frame'
                    }]
    )

    visual_slam_launch_container = ComposableNodeContainer(
        name='visual_slam_launch_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            visual_slam_node
        ],
        output='screen'
    )

    return launch.LaunchDescription([visual_slam_launch_container])