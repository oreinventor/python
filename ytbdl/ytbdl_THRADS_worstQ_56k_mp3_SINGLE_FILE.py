import youtube_dl
import _thread
import time

def running_workers(thread_pool):
	while(1):
		time.sleep(10)
		print("No of threads = " + str(len(thread_pool)))
	

def worker_thread(url,thread_pool):
	options={
		'format':'worstaudio',
		'outtmpl':folder_path+'/%(title)s.%(ext)s',
                'quiet':True,
        'postprocessors':[{
         'key':'FFmpegExtractAudio',
         'preferredcodec':'mp3',
         'preferredquality':'56',
         }],}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([url])
	thread_pool.pop()

threads=int(input('Enter no threads : '))
url=input('Enter URL : ')
start=int(input('Enter the initial # of video of the playlist : '))
folder_path=input("Enter destination folder : ")



with youtube_dl.YoutubeDL() as ydl:
	linkList = ydl.extract_info(url,download=False);

thread_pool=set()

_thread.start_new_thread(running_workers,(thread_pool, ) )

i=start
worker_thread(url,thread_pool)
'''
while(i<len(linkList['entries']) ) :
	if (len(thread_pool)<threads) :
		print('Starting thread no ' + str(i) )
		thread_pool.add( _thread.start_new_thread(worker_thread,(linkList['entries'][i]['webpage_url'],thread_pool, ) ) )
		i+=1
	else:
		time.sleep(2)
'''
