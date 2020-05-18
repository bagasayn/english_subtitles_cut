import os
import subprocess as sp
import sys
from datetime import time

from moviepy.config import get_setting
from moviepy.tools import subprocess_call

def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ Makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    name, ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, T1, T2, ext)
    
    cmd = [get_setting("FFMPEG_BINARY"),"-y",
           "-ss", "%0.2f"%t1,
           "-i", filename,
           "-t", "%0.2f"%(t2-t1),
           "-map", "0", "-vcodec", "copy", "-acodec", "copy", targetname]
    
    subprocess_call(cmd)


name=sys.argv[1]
Str_start = time.fromisoformat(("{0}".format(sys.argv[2])).replace(',','.'))
Str_end = time.fromisoformat(("{0}".format(sys.argv[3])).replace(',','.'))

start=Str_start.hour * 3600 + Str_start.minute * 60 + Str_start.second
end=Str_end.hour * 3600 + Str_end.minute * 60 + Str_end.second


ffmpeg_extract_subclip('{0}'.format(name),start,end,'Cut-{0}'.format(name))


