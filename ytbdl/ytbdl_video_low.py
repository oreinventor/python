import youtube_dl
from getlinks import *
import _thread
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
        'format':'mp4[height<360]+worstaudio/worst',
        #'keepvideo':False,
        'outtmpl':filename,

    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))

if __name__=='__main__':
    #run()
	#
	#
	threads=int(input('No of threads '))
	url=input('enter video url ')
	for i in range(0,threads):
		_thread.start_new_thread(getvideo,(url,))
