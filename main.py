import pytube

url = input("Enter video URL: ")

path = input("Enter download path (leave empty for current directory): ")

# Check if the path is provided, otherwise use the current directory
if path == "":
    path = "./"

# Download the video with the highest resolution
pytube.YouTube(url).streams.get_highest_resolution().download(path)