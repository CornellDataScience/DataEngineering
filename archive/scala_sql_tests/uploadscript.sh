#!/usr/bin/env bash

# DO NOT MODIFY ABOVE THIS LINE

#For the following two variables, 
#set your remote login username, the URL to the remote server
#For example:
#	USERNAME=johndoe
#	REMOTE=test.url.com

USERNAME=haramkim
REMOTE=localhost

# DO NOT MODIFY BELOW THIS LINE

CURRENT=$(basename $(pwd))
REMDIR=MyUploads/"$USER"/"$CURRENT"/
CMD="mkdir -p ~/${REMDIR}"
 
ssh "$USERNAME"@"$REMOTE" $CMD
rsync  -r -v -e ssh . "$USERNAME"@"$REMOTE":"$REMDIR"

echo
echo "Uploaded files to: ${REMDIR}"