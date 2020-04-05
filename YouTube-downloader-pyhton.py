#Importing the desired libraries.
from pytube import YouTube

#Basic Description.

print("_______________________________________________")
print("_______________________________________________")
print('\n\n');
print("WELCOME TO THE YTDLR!")
print("\n")
print("This is a simple tool to download any video on YouTube.")
print("All you have to do is paste the link in the prompt, specify the path and resolution. Your video will be downloaded.")
print('\n');

#User inputs.
link = input("Please enter the link of the YouTube video: ")
print('------------------------')
print('Please specify the path (Example: D:/YouTube) where you want to store the downloaded video file.') 
print('If you press ENTER, the CWD is selected by default.')
path = input("Path = ")
print('------------------------')
print('Specify the required resolution. Choose one of them: 360p, 720p, 1080p.')
resolution = input("Resolution = ")
print('------------------------')

try:
	yt = YouTube(link)
except:
	print("Couldn't create the YouTube object. Please check your Internet Connection and try again.")

#Choosing the right stream based on user requirements.
streams = yt.streams.filter(res = resolution)
#Choosing the first stream among the available ones.
stream = streams.first()


#Starting the download.
try:
	print("\nBeginning the download. Please have some patience. This may take a few minutes depending on your Internet Connection.\n")
	stream.download(path)
	print("\nDownload complete.")
except:
	print("Couldn't download the video. Please check your internet connection and try again.")
	print("Or maybe try requesting for a different resolution.")