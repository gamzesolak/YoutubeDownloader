import pytube

url = input("enter video url: ")
path = ""
pytube.YouTube(url).streams.get_audio_only().download(path)
