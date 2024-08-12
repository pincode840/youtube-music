from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]
# Function to download YouTube videos from a list of URLs
def download_videos(urls):
    for url in urls:
        try:
            yt = YouTube(url)
            print("Downloading:", yt.title)
            yt.streams.get_highest_resolution().download()
            print("Download completed for:", yt.title)
        except Exception as e:
            print("Error downloading", url, ":", e)

# List of YouTube video URLs
video_urls = [
    'https://youtu.be/QlLgNoo3dGQ?si=YwHCGr7rSpq5P0hU'
]

# Call the function with the list of URLs
download_videos(video_urls)

print("All downloads completed!")
