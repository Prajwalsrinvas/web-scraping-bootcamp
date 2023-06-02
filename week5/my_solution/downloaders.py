import asyncio
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import aiohttp
import requests
from tqdm.auto import tqdm


def download_images_requests(keyword, image_links, image_count, BASE_FOLDER):
    image_links = image_links[:image_count]
    print(f"[x] Downloading {len(image_links)} images")
    for index, image_link in tqdm(
        enumerate(image_links, start=1),
        desc="Downloading images",
        total=len(image_links),
    ):
        response = requests.get(image_link)
        response.raise_for_status()
        image_path = os.path.join(BASE_FOLDER, keyword, f"{keyword}_{index}.jpg")
        with open(image_path, "wb") as f:
            f.write(response.content)


def download_images_requests_session(keyword, image_links, image_count, BASE_FOLDER):
    image_links = image_links[:image_count]
    print(f"[x] Downloading {len(image_links)} images")
    session = requests.Session()
    for index, image_link in tqdm(
        enumerate(image_links, start=1),
        desc="Downloading images",
        total=len(image_links),
    ):
        response = session.get(image_link)
        response.raise_for_status()
        image_path = os.path.join(BASE_FOLDER, keyword, f"{keyword}_{index}.jpg")
        with open(image_path, "wb") as f:
            f.write(response.content)


async def download_image_aiohttp(session, image_link, image_path):
    async with session.get(image_link) as response:
        response.raise_for_status()
        with open(image_path, "wb") as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)


async def download_images_aiohttp(keyword, image_links, image_count, BASE_FOLDER):
    image_links = image_links[:image_count]
    print(f"[x] Downloading {len(image_links)} images")

    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, image_link in enumerate(image_links, start=1):
            image_path = os.path.join(BASE_FOLDER, keyword, f"{keyword}_{index}.jpg")
            task = asyncio.create_task(
                download_image_aiohttp(session, image_link, image_path)
            )
            tasks.append(task)

        await asyncio.gather(*tasks)


def download_image_threadpoolexecutor(image_link, keyword, index, BASE_FOLDER):
    response = requests.get(image_link)
    response.raise_for_status()
    image_path = os.path.join(BASE_FOLDER, keyword, f"{keyword}_{index}.jpg")
    with open(image_path, "wb") as f:
        f.write(response.content)


def download_images_threadpoolexecutor(keyword, image_links, image_count, BASE_FOLDER):
    image_links = image_links[:image_count]
    print(f"[x] Downloading {len(image_links)} images")

    with ThreadPoolExecutor() as executor:
        futures = []
        for index, image_link in enumerate(image_links, start=1):
            future = executor.submit(
                download_image_threadpoolexecutor,
                image_link,
                keyword,
                index,
                BASE_FOLDER,
            )
            futures.append(future)

        for future in tqdm(
            as_completed(futures), desc="Downloading images", total=len(futures)
        ):
            future.result()
