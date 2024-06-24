from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import yt_dlp

def get_video_urls(channel_url):
    video_urls = set()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(channel_url + "/videos")

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    while True:
        for a in driver.find_elements(By.XPATH, '//a[@href]'):
            href = a.get_attribute('href')
            if '/watch?v=' in href:
                video_urls.add(href)
        
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    driver.quit()
    return list(video_urls)

def download_videos(video_urls):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_urls)

# Replace with your channel URL
channel_url = "https://www.youtube.com/channel/YOUR_CHANNEL_ID"
urls = get_video_urls(channel_url)
for url in urls:
    print(url)

# Download the videos
download_videos(urls)
