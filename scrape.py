import hashlib, io, requests, pandas as pd
from lib2to3.pgen2 import driver
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pathlib import Path
from PIL import Image


# Base Url
def get_content_from_url(url):
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    content = driver.page_source
    driver.quit()
    return content

def parse_image_urls(content,classes, location, source):
    soup = BeautifulSoup(content, "html.parser")
    results=[]
    for a in soup.findAll(attrs={'class': classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results

def save_urls(image_urls):
    df = pd.DataFrame({"links":image_urls})
    df.to_csv("links.csv", index=False,encoding="utf-8")

def get_and_save_image_to_file(image_url, output_dir):
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")
    file_name = hashlib.sha1(image_content).hexdigest()[:10] + ".png"
    file_path = output_dir/file_name
    image.save(file_path, "PNG", quality=80)

def main():
    base_url = "https://www.grailed.com/designers/yohji-yamamoto"
    content = get_content_from_url(base_url)
    image_urls = parse_image_urls(
        content=content, classes="listing-cover-photo", location="img", source="src"
    )
    save_urls(image_urls)

    for image_url in image_urls:
        get_and_save_image_to_file(image_url, output_dir=Path('./images'))

if __name__ == "__main__":
    main()
    print("done")
