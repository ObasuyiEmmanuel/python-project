from pytube import YouTube

Link = input("enter the link: ")
check = input("video download press 1\nAudio download press 2\nEnter choice: ")

if check == "1":
    youtube_1 = YouTube(Link)
    videos = youtube_1.streams.filter(progressive=True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    strm = int(input("please provide your index you want to download: "))
    videos[strm].download()
    print("successfully download")

elif check == "2":
    youtube_2 = YouTube(Link)
    audio = youtube_2.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    strm2 = int(input("type your index that you want to download: "))
    audio[strm2].download()
    print("successfully downloaded")