from pytube import YouTube

# Prompt user to enter YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()
