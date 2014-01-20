import sys, os, zipfile

def zip(src, dst):														#src on disc. dst is zip file
	zf = zipfile.ZipFile("%s.zip" % (dst), "w")							#create zip
	
	absFilePath = os.path.abspath(src)									#get path of src (/home/chris/test)
	
	for dirname, subdirs, files in os.walk(src):						#for this dir and each subdir/file in src
		for filename in files:											#for each file in file list from walk
			absname = os.path.abspath(os.path.join(dirname, filename))	#get the path+name of file
			arcname = absname[len(absFilePath) + 1:]					#get location in zip (e.g. no /home or /var dir)
			zf.write(absname, arcname)									#write each file from absname(loc on disc) to arcname(new loc in zip)
	zf.close()															#close zip file
	
	
zip(sys.argv[1], sys.argv[2])

