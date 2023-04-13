import pytube
url=input("url: ")
path=""   #direkt buraya kaydet
pytube.YouTube(url).streams.get_highest_resolution().download(path)
