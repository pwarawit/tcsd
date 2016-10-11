#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage example:
# python channel.py --channel_id='<channel_id>'

import httplib2
import os
import sys
import json

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# DEVELOPER_KEY = "AIzaSyBRM1lDMkC8u_UsMOIM9j0Df0B9oC9rPKU" # (TCSD2Social)
DEVELOPER_KEY = "AIzaSyArZEg4nMfnWbmtP-_Hxd7LWHsRK29QRWE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Call the API's channels.list method to retrieve an existing channel data.
# This method will write to the ..\data\yt_channel\ folder with json file.
def get_channel_list(youtube, channel_id):
  results = youtube.channels().list(
    part="contentDetails, contentOwnerDetails, localizations, snippet, statistics, status, topicDetails",
    id=channel_id,
	maxResults=50
  ).execute()
  
  with open('c:\\tcsd\\data\\yt_channel\\'+ channel_id +'.json','w') as outfile:
	json.dump(results, outfile)
	

if __name__ == "__main__":
  # The "channel_id" option specifies the ID of the selected YouTube channel.
  argparser.add_argument("--channel_id", help="ID for channel for which the localization will be applied.")
	
  args = argparser.parse_args()

  if not args.channel_id:
    exit("Please specify channel id using the --channel_id= parameter.")

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  
  try:
	get_channel_list(youtube, args.channel_id)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  else:
    print ""