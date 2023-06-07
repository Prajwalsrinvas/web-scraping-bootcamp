
<h1 align="center">Unsplash image downloader</h1>

## 📍Overview

The project provides a set of tools for web scraping Unsplash for free images based on a keyword. It offers various image download functions that use different libraries to download images concurrently and includes options to benchmark the performance of each download method. The project's value proposition lies in its ability to provide a comprehensive set of tools for image downloads and benchmarking that can help users make informed decisions about the most efficient download method for their needs.

---
## 💻 Modules

Here's the modified table with the "Module" column removed:

| File                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| plot_perf_benchmark.py       | The code defines a function to plot data from a CSV file into a horizontal bar graph. The data is extracted and sorted before being plotted with xkcd styling. The function also saves the plot as an image file and displays the graph.                                                                                                                                                                                     |
| unsplash_image_downloader.py | The provided code is an image downloader that scrapes Unsplash for free images based on a given keyword and downloads them using four different methods-requests, requests session, aiohttp, and threadpoolexecutor. It includes an option to benchmark all downloader methods and output a performance report with a plot. The code also provides an argparse interface for user input.                                     |
| downloaders.py               | The provided code snippet offers four different image download functions that use various libraries and techniques such as requests, aiohttp, and ThreadPoolExecutor to download images concurrently. These functions take a keyword, a list of image links, and the number of images to download, and save the images in a specified base folder. The tqdm library is used to display progress bars during image downloads. |

<br>

---

## 📸 Screenshots

### 1. Downloading 5 redpanda images from unsplash

```
python unsplash_image_downloader.py --keyword redpanda --image_count 5
```

![](assets/unsplash_dl_demo.gif)

### 2. Downloading 30 spider images from unsplash

```
python unsplash_image_downloader.py --keyword spider --image_count 30 --benchmark 3
```

 - The same set of images is downloaded using all download methods.
 - This is repeated 3 times to get an average of the elapsed time.
 - The benchmark scores are stored as a CSV.
 - The benchmark scores CSV is plotted, and the plot is saved to a file.


![](assets/benchmark.gif)

#### Downloaded images
![](assets/downloaded_images.png)

#### Performance benchmark scores saved as csv and plot saved as png
![](assets/perf_benchmark.png)

#### Performance benchmark:

|crawler_type      |test_1            |test_2            |test_3            |average_time      |
|------------------|------------------|------------------|------------------|------------------|
|requests          |43.77858924865723 |19.471466779708862|18.428603649139404|27.22621989250183 |
|requests_session  |22.73876166343689 |15.675415992736816|15.866717338562012|18.093631664911907|
|aiohttp           |11.308744192123413|5.796777725219727 |6.504941940307617 |7.870154619216919 |
|threadpoolexecutor|6.401994228363037 |6.347405433654785 |6.207687854766846 |6.319029172261556 |

![](perf_benchmark/2023_05_31_19_57_32/performance_plot.png)

### 3. Downloading 75 tarantula images from unsplash

```
python unsplash_image_downloader.py --keyword tarantula --image_count 75 --benchmark 2
```
#### Performance benchmark:

|crawler_type      |test_1            |test_2            |average_time      |
|------------------|------------------|------------------|------------------|
|requests          |86.94784784317017 |76.76719880104065 |81.85752332210541 |
|requests_session  |52.317723512649536|56.81423902511597 |54.56598126888275 |
|aiohttp           |17.783081531524658|21.12917923927307 |19.456130385398865|
|threadpoolexecutor|19.55467414855957 |23.745527029037476|21.650100588798523|

![](perf_benchmark/2023_05_31_20_23_31/performance_plot.png)
