import os

import matplotlib.pyplot as plt
import pandas as pd


def plot_perf_benchmark(file_path, current_time, image_count, keyword):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Extract the necessary columns from the DataFrame
    crawler_types = data["crawler_type"]
    average_times = data["average_time"]

    # Sort the data in ascending order of average times
    sorted_indices = average_times.argsort()
    crawler_types = crawler_types[sorted_indices]
    average_times = average_times[sorted_indices]

    # Set up xkcd styling
    # refer this to get the font to work:
    # https://stackoverflow.com/questions/19663986/getting-xkcd-plots-using-matplotlib/22812176#22812176
    plt.xkcd()

    # Create the horizontal bar graph
    plt.barh(crawler_types, average_times, color="blue")

    # Set labels and title
    plt.xlabel("Time (in secs)")
    plt.ylabel("Crawler Types")
    plt.title(f"Time taken to download {image_count} {keyword} images from unsplash")

    # Add value annotations to the graph
    for index, value in enumerate(average_times):
        plt.text(
            x=value + 0.02,
            y=index,
            s=str(round(value, 2)) + "s",
            color="black",
            va="center",
            ha="left",
        )

    # Save the plot to a file with high clarity
    file_path = os.path.join(
        "perf_benchmark",
        current_time,
        "performance_plot.png",
    )
    plt.savefig(file_path, dpi=600, bbox_inches="tight")

    # Display the graph
    plt.show()
