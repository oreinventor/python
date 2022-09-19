import youtube_dl
from getlinks import *
def run():
        video_url = input("please enter youtube video url:")
        videolist=getlinks(video_url)
        for videolink in videolist:
                try:
                        getvideo(videolink)
                except:
                        continue
def getvideo(link):
    video_url=link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = format(video_info['title']) + ".mp4"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
        'postprocessors': [{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'320',
                }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
