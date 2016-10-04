#!/usr/bin/python

# Usage example:
# python channel_list.py --channel_id='<channel_id>'

import httplib2
import os
import sys
import json

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
DEVELOPER_KEY = "AIzaSyArZEg4nMfnWbmtP-_Hxd7LWHsRK29QRWE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


# Call the API's channels.list method to retrieve an existing channel localization.
# If the localized text is not available in the requested language,
# this method will return text in the default language.
def get_channel_list(youtube, channel_id, language):
  results = youtube.channels().list(
    #part="snippet",
	part="contentDetails, contentOwnerDetails, localizations, snippet, statistics, status, topicDetails",
    id=channel_id,
	hl=language
  ).execute()
  
  #json1 = json.dumps(results, ensure_ascii=False)
  with open('test.json','w') as outfile:
	json.dump(results, outfile)
  #print json1

  # print channel_id
  # print results
  # The localized object contains localized text if the hl parameter specified
  # a language for which localized text is available. Otherwise, the localized
  # object will contain metadata in the default language.
  #localized = results["items"][0]["snippet"]["localized"]
  #print results["items"][0]

  #print "Channel description is '%s' in language '%s'" % (localized["description"], language)
	

# Call the API's channels.list method to list the existing channel localizations.
def list_channel_localizations(youtube, channel_id):
  results = youtube.channels().list(
    part="snippet,localizations",
    id=channel_id
  ).execute()

  localizations = results["items"][0]["localizations"]

  for language, localization in localizations.iteritems():
    print "Channel description is '%s' in language '%s'" % (localization["description"], language)


if __name__ == "__main__":
  # The "channel_id" option specifies the ID of the selected YouTube channel.
  argparser.add_argument("--channel_id",
    help="ID for channel for which the localization will be applied.")
  argparser.add_argument("--default_language", help="Default language of the channel to update.",
    default="en")
  # The "language" option specifies the language of the localization that is being processed.
  argparser.add_argument("--language", help="Language of the localization.", default="th")
  # The "description" option specifies the localized description of the chanel to be set.
	
  args = argparser.parse_args()

  if not args.channel_id:
    exit("Please specify channel id using the --channel_id= parameter.")

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  try:
	get_channel_list(youtube, args.channel_id, args.language)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  else:
    #print "Set and retrieved localized metadata for a channel."
	print ""