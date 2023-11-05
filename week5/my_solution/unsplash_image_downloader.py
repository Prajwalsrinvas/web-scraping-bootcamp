import argparse
import asyncio
import os
import time
from datetime import datetime

import jmespath as jp
import pandas as pd
import requests
from downloaders import (download_images_aiohttp, download_images_requests,
                         download_images_requests_session,
                         download_images_threadpoolexecutor)
from plot_perf_benchmark import plot_perf_benchmark
from tqdm.auto import tqdm


def hit_unsplash_api(keyword, page=1):
    headers = {
        "authority": "unsplash.com",
        "accept": "*/*",
        "accept-language": "en-US",
        "referer": "https://unsplash.com/s/photos/pandas",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    params = {
        "query": keyword,
        "per_page": "10",
        "page": f"{page}",
    }
    response = requests.get(
        "https://unsplash.com/napi/search/photos", params=params, headers=headers
    )
    response.raise_for_status()
    data = response.json()
    jmes_path = "results[?premium==`false`].links.download"
    image_links = jp.search(jmes_path, data)
    return image_links


def get_image_links(keyword, image_count):
    images_per_page = 8  ## page returns 10 images, but 2 are premium
    all_image_links = []

    print(f"[x] {keyword=}")
    pages_to_crawl = (image_count // images_per_page) + 1
    print(f"[x] {pages_to_crawl=}")

    if image_count < images_per_page:
        image_links = hit_unsplash_api(keyword)
        all_image_links.extend(image_links)
    else:
        for page in tqdm(
            range(1, pages_to_crawl + 1),
            desc="Getting links",
        ):
            image_links = hit_unsplash_api(keyword, page=page)
            all_image_links.extend(image_links)

    print(f"[x] Found {len(all_image_links)} '{keyword}' free images\n")
    return all_image_links


def download_images(keyword, image_count):
    image_links = get_image_links(keyword, image_count)
    crawl_stats = {}
    for download_method_name, download_method in download_methods.items():
        start_time = time.time()
        print(f"\n\n[x] Download method: {download_method_name}")
        BASE_FOLDER = os.path.join("images", download_method_name)
        keyword = keyword.lower().replace(" ", "_")
        os.makedirs(os.path.join(BASE_FOLDER, keyword), exist_ok=True)

        if download_method_name == "aiohttp":
            asyncio.run(download_method(keyword, image_links, image_count, BASE_FOLDER))
        else:
            download_method(keyword, image_links, image_count, BASE_FOLDER)

        elapsed_time = time.time() - start_time
        crawl_stats[download_method_name] = elapsed_time
    return crawl_stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Downloader")
    parser.add_argument(
        "--keyword",
        type=str,
        help="Search term for the image to download",
        required=True,
    )
    parser.add_argument(
        "--image_count", type=int, help="Number of images to download", required=True
    )
    parser.add_argument(
        "--benchmark_times",
        type=int,
        help="Number of times to run benchmark. All downloader methods will be used when this is used.",
        required=False,
    )

    args = parser.parse_args()

    keyword = args.keyword
    image_count = args.image_count
    benchmark_times = args.benchmark_times
    all_crawl_stats = []
    download_methods = {
        "requests": download_images_requests,
        "requests_session": download_images_requests_session,
        "aiohttp": download_images_aiohttp,
        "threadpoolexecutor": download_images_threadpoolexecutor,
    }
    if not benchmark_times:
        required_methods = ["requests_session"]
        download_methods = {
            k: v for k, v in download_methods.items() if k in required_methods
        }

    if not benchmark_times:
        download_images(keyword, image_count)
    else:
        for attempt in range(1, benchmark_times + 1):
            print(f"\n[x] {attempt=}")
            crawl_stats = download_images(keyword, image_count)
            all_crawl_stats.append(crawl_stats)
        all_crawl_stats_df = pd.DataFrame(all_crawl_stats).T
        all_crawl_stats_df["average_time"] = all_crawl_stats_df.mean(axis=1)

        columns = (
            ["crawler_type"]
            + [f"test_{i}" for i in range(1, benchmark_times + 1)]
            + ["average_time"]
        )
        all_crawl_stats_df.reset_index(level=0, inplace=True)
        current_time = f"{datetime.now():%Y_%m_%d_%H_%M_%S}"
        os.makedirs(os.path.join("perf_benchmark", current_time))
        file_path = os.path.join("perf_benchmark", current_time, "perf_benchmark.csv")
        all_crawl_stats_df.to_csv(file_path, header=columns, index=False)
        plot_perf_benchmark(file_path, current_time, image_count, keyword)
