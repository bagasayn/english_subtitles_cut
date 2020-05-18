import subprocess as sp
import sys as s

sp.run(["youtube-dl","--all-subs","--skip-download","{0}".format(s.argv[1])])
