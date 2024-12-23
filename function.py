import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def input_parameters():
    # Display sliders and inputs for parameters
    st.title("Input Parameters for Video Data Estimation")
 
    # Input for full video time
    full_video_time = st.slider(
        "Full Video Time (hours)",
        min_value=0.5,
        max_value=5.0,
        value=1.5,
        step=0.1
    )
 
    # Input for data usage per hour
    data_per_hour = st.slider(
        "Data Usage per Hour (GB)",
        min_value=0.5,
        max_value=5.0,
        value=1.6,
        step=0.1
    )
 
    # Input for number of flips range
    num_flips_min = st.number_input(
        "Minimum Number of Flips",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )
    num_flips_max = st.number_input(
        "Maximum Number of Flips",
        min_value=1,
        max_value=10,
        value=5,
        step=1
    )
    num_flips_range = range(num_flips_min, num_flips_max + 1)
 
    # Input for flip time range
    flip_time_min = st.number_input(
        "Minimum Flip Time (minutes)",
        min_value=1,
        max_value=60,
        value=3,
        step=1
    )
    flip_time_max = st.number_input(
        "Maximum Flip Time (minutes)",
        min_value=1,
        max_value=60,
        value=5,
        step=1
    )
    flip_time_range = range(flip_time_min, flip_time_max + 1)
 
    # Input for number of devices range
    num_devices_min = st.number_input(
        "Minimum Number of Devices",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )
    num_devices_max = st.number_input(
        "Maximum Number of Devices",
        min_value=1,
        max_value=10,
        value=5,
        step=1
    )
    num_devices_range = range(num_devices_min, num_devices_max + 1)
 
    # Return all the parameters
    return full_video_time, data_per_hour, num_flips_range, flip_time_range, num_devices_range


# Function to perform calculations
def calculate_data(name, running_time, movie_length, resolution, downstream_speed, upstream_speed):
    # Calculate Total Data Usage
    total_data_usage_downstream = downstream_speed * 60 * 60 / 8  # MB per hour
    total_data_usage_upstream = upstream_speed * 60 * 60 / 8  # MB per hour
    
    # Calculate Average Bandwidth Downstream (Mbps)
    avg_bandwidth_downstream = downstream_speed
    
    # Estimated Buffer Data Usage (MB) and Buffer Time (HH:MM)
    buffer_time = "00:15"  # Assume a fixed buffer time
    buffer_data_usage = avg_bandwidth_downstream * 60 * 15 / 8  # MB for 15 minutes

    # Return results as a dictionary
    return {
        "Name": name,
        "Running Time": running_time,
        "Movie Length (Seconds)": movie_length,
        "Resolution": resolution,
        "SpeedTest Downstream Value (Mbps)": downstream_speed,
        "SpeedTest Upstream Value (Mbps)": upstream_speed,
        "Total Data Usage per Hour (Downstream) (MB)": total_data_usage_downstream,
        "Total Data Usage per Hour (Upstream) (MB)": total_data_usage_upstream,
        "Average Bandwidth Downstream (Mbps)": avg_bandwidth_downstream,
        "Estimated Buffer Data Usage (MB)": buffer_data_usage,
    }