import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from function import input_parameters, calculate_data
# # Main Streamlit App
# def main():
#     full_video_time, data_per_hour, num_flips_range, flip_time_range, num_devices_range = input_parameters()
 
#     st.subheader("Selected Parameters:")
#     st.write(f"Full Video Time: {full_video_time} hours")
#     st.write(f"Data per Hour: {data_per_hour} GB")
#     st.write(f"Number of Flips Range: {list(num_flips_range)}")
#     st.write(f"Flip Time Range: {list(flip_time_range)} minutes")
#     st.write(f"Number of Devices Range: {list(num_devices_range)}")
 
# if __name__ == "__main__":
#     main()
# Initialize an empty DataFrame to store results
if "results_data" not in st.session_state:
    st.session_state["results_data"] = pd.DataFrame()

def main():
    st.title("Streaming Data Usage Calculator")

    # Input: Name and Streaming Details
    name = st.text_input("Name of the person running:")
    running_time = st.text_input("Running Time (HH:MM):", "12:00")
    movie_length = st.number_input("Movie Length (seconds):", min_value=300, max_value=10000, value=4800, step=10)
    resolution = st.selectbox("Resolution Setting:", ["HD", "SD", "4K"])
    downstream_speed = st.number_input("SpeedTest Downstream Value (Mbps):", min_value=0.1, max_value=1000.0, value=100.0, step=0.1)
    upstream_speed = st.number_input("SpeedTest Upstream Value (Mbps):", min_value=0.1, max_value=1000.0, value=50.0, step=0.1)

    # Calculate Results
    if st.button("Calculate"):
        results = calculate_data(name, running_time, movie_length, resolution, downstream_speed, upstream_speed)

        # Display Results as a DataFrame
        results_df = pd.DataFrame([results])
        st.subheader("Calculated Results:")
        st.dataframe(results_df)

        # # Option to Save Results
        # if st.button("Save Results"):
        #     # Append new results to the session state DataFrame
        #     st.session_state["results_data"] = pd.concat(
        #         [st.session_state["results_data"], results_df], ignore_index=True
        #     )
        #     st.success("Results saved successfully!")

    # Show All Saved Results
    if not st.session_state["results_data"].empty:
        st.subheader("All Saved Calculations:")
        st.dataframe(st.session_state["results_data"])

        # Download Option
        csv = st.session_state["results_data"].to_csv(index=False)
        st.download_button("Download Results as CSV", data=csv, file_name="streaming_data_results.csv", mime="text/csv")

    # Visualization: Bar Chart
    if not st.session_state["results_data"].empty:
        st.subheader("Visualization: Total Data Usage per Hour (Downstream)")
        fig, ax = plt.subplots()
        ax.bar(
            st.session_state["results_data"].index + 1,
            st.session_state["results_data"]["Total Data Usage per Hour (Downstream) (MB)"],
            color="blue"
        )
        ax.set_title("Total Data Usage per Hour")
        ax.set_xlabel("Instance")
        ax.set_ylabel("Data Usage (MB)")
        for i, v in enumerate(st.session_state["results_data"]["Total Data Usage per Hour (Downstream) (MB)"]):
            ax.text(i + 1, v + 10, f"{v:.2f}", ha="center")
        st.pyplot(fig)

if __name__ == "__main__":
    main()








