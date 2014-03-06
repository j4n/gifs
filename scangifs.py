#!/usr/bin/python
#vim:ts=2:sw=2:expandtabs
import fnmatch
import os
import glob
import json

gifdir = "/silo/share/gifs"
outfile = os.path.join(gifdir,"gifs.json");

gifs = []
for gif in glob.iglob(os.path.join(gifdir, "*", "*.gif")):
	gifs.append(gif[len(gifdir)+1:]) # cut off gifdir
f = open(outfile, 'w')
f.write(json.dumps({'gifs': gifs}))
f.close
