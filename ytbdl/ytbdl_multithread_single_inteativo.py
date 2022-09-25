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
def getvideo(link,video,audio):
    video_url=link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = format(video_info['title']) + ".mp4"
    options={
        'format':'bestvideo[height<='+video+']+'+audio+'audio',
        #'keepvideo':False,
        'quiet':True,
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
	v_quality=input('Video Quality ( 144,240,360,480,720,1080) ')
	a_quality=input('Audio Quality (worst / best) ')
	for i in range(0,threads):
		_thread.start_new_thread(getvideo,(url,v_quality,a_quality,))
