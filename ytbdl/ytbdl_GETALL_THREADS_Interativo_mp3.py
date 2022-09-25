import youtube_dl
import urllib.request as req
import _thread
import os

def getplaylists(url):
    data=req.urlopen(url).read().decode()
    videolist=set()
    b=0
    while(True):
        try:
            urlStr='www.youtube.com/watch?v'
            a=data.index("/watch?v=",b+1)
            b=data.index(",",a)
            c=data.index("list=",a)
            urlStr+=data[a+8:b][0:12]
            urlStr+='&'+data[c:b-1]
            videolist.add(urlStr)
        except:
            break
    print(videolist)
    return videolist

def callProcess(argstr):
    os.system('python '+'ytbdl_GETALL_THREADS_Interativo_mp3_Module.py '+argstr)

url=input('Entre com a url : ')
threads=input('Enter no threads : ')
quality=input('Entre qualidade\n 0 - worst\n 1 - best : ')
folder=input('Entre destination folder : ')
if quality=='0':
    quality='worst'
else:
    quality='best'
videolist=getplaylists(url)
for v in videolist:
    argstr='-threads '+threads+' -quality '+quality+' -folder '+folder+' -url \"'+v+"\""
    print(argstr)
    _thread.start_new_thread(callProcess,(argstr,))
