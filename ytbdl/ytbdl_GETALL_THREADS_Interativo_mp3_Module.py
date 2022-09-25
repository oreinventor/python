import youtube_dl
import _thread
import time
import sys

def running_workers(thread_pool):
	while(1):
		time.sleep(10)
		print("No of threads = " + str(len(thread_pool)))
	

def worker_thread(url,thread_pool):
	options={
		'format':quality+'audio',
                'quiet':True,
         #'outtmpl':folder_path+'/%(title)s.mp3', 
         'outtmpl':folder+'/%(title)s.%(ext)s',
         'postprocessors':[{
         'key':'FFmpegExtractAudio',
         'preferredcodec':'mp3',
         'preferredquality':bitrate,
         }],
         }
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([url])
	thread_pool.pop()

threads=0
quality,url,folder='','',''
bitrate='8'

for i in range(1,len(sys.argv)):
    #print(sys.argv[i])
    if sys.argv[i]=='-threads':
        threads=int(sys.argv[i+1])
    if sys.argv[i]=='-folder':
        folder=sys.argv[i+1]
    if sys.argv[i]=='-url':
        url=sys.argv[i+1]
    if sys.argv[i]=='-quality':
        quality=sys.argv[i+1]

#print(threads,quality,url,folder)

playliststart=0

if quality=='best':
    bitrate='160'
else:
    bitrate='56'

with youtube_dl.YoutubeDL() as ydl:
    linkList = ydl.extract_info(url, download=False);

thread_pool=set()

_thread.start_new_thread(running_workers,(thread_pool, ) )

i=int(playliststart)
while(i<len(linkList['entries']) ) :
	if (len(thread_pool)<threads) :
		print('Starting thread no ' + str(i) )
		thread_pool.add( _thread.start_new_thread(worker_thread,(linkList['entries'][i]['webpage_url'],thread_pool, ) ) )
		i+=1
	else:
		time.sleep(2)
