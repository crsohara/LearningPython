import dropbox, os, sys, zipfile

app_key = '<your app_key>'												#generated by dropbox dev app center
app_secret = '<your app_secret>'											#generated by dropbox dev app center
accessTokenFile = 'dropbox_access_token_file'

def zip(src, dst):														#src on disc. dst is zip file
	zf = zipfile.ZipFile("%s.zip" % (dst), "w")							#create zip
	
	absFilePath = os.path.abspath(src)									#get path of src (/home/chris/test)
	
	for dirname, subdirs, files in os.walk(src):						#for this dir and each subdir/file in src
		for filename in files:											#for each file in file list from walk
			absname = os.path.abspath(os.path.join(dirname, filename))	#get the path+name of file
			arcname = absname[len(absFilePath) + 1:]					#get location in zip (e.g. no /home or /var dir)
			zf.write(absname, arcname)									#write each file from absname(loc on disc) to arcname(new loc in zip)
	zf.close()															#close zip file
	

def writeToFile(filename, access_token):											#write access_token to file
	try:
		with  open('dropbox_access_token_file', 'w') as accessCodeFile:
			accessCodeFile.write(access_token)
		accessCodeFile.close()
	except IOError:
		msg = "Error: Unable to write access code to file"


def getAccessToken(authorize_url, accessTokenFile, flow):
	if not (os.path.isfile(os.path.abspath(accessTokenFile))):					#check if access code file exists(i.e. app has be authorized already)
		print 'Go to ' + authorize_url + ', allow and copy auth code'			#if not, go through auth process and save access token to file
		auth_code = raw_input ("Enter the authorization code now: ").strip()
		access_token, user_id = flow.finish(auth_code)

		writeToFile(accessTokenFile, access_token)

	else:																		#app has already been authorized
		accessCodeFile = open(accessTokenFile, 'r')								#read access token from file  
		access_token = accessCodeFile.read()
		access_token = access_token.rstrip()									#strip '\n' from end of line containing access token
		
	return access_token


def main():
	
	zip(sys.argv[1], '/tmp/file')
	
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()

	access_token = getAccessToken(authorize_url, accessTokenFile, flow)

	client = dropbox.client.DropboxClient(access_token)
	#print 'linked account', client.account_info()								#show account info

	f = open('/tmp/file.zip')
	response = client.put_file('/file.zip', f)									#upload file to dropbox
	os.remove('/tmp/file.zip')													#remove zip file from tmp directory
	print "uploaded: ", response


if __name__ == "__main__":
	main()
