#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage example:
# python video.py --video_id='<video_id>'

import sys
import json

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyArZEg4nMfnWbmtP-_Hxd7LWHsRK29QRWE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Call the API's activities.list method to retrieve an existing channel data.
# This method will write to the ..\data\yt_channel\ folder with json file.
def get_video(youtube, video_id):
  results = youtube.videos().list(
    part="contentDetails, id, localizations, player, snippet, statistics, status, topicDetails",
	id=video_id
  ).execute()
  
  with open('..\\data\\yt_video\\'+ video_id +'.json','w') as outfile:
	json.dump(results, outfile)

if __name__ == "__main__":
  # The "channel_id" option specifies the ID of the selected YouTube channel.
  argparser.add_argument("--video_id", help="ID for video for which comment threads will be extracted.")
  args = argparser.parse_args()

  if not args.video_id:
    exit("Please specify video id using the --video_id= parameter.")

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  
  try:
	get_video(youtube, args.video_id)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  else:
    print ""
