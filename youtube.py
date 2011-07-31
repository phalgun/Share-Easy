import gdata.youtube
import gdata.geo
import gdata.youtube.service
import gdata.media
import re
import globals

'''
    Function uploads a video pointed by filename to YouTube
    It returns the Url of the uploaded video
'''
def post_to_youtube(filename,video_title,username=None,password=None) :
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    if globals.youtube_username is None or globals.youtube_password is None:
        # call UI .. set the username and password
        # Store them in globals.youtube_*
        # just in case, its taken as func arguments now
        globals.youtube_username = username
        globals.youtube_password = password
    
    yt_service.email = globals.youtube_username
    yt_service.password = globals.youtube_password

    yt_service.source = 'youtube_uploader'
    yt_service.developer_key = 'AI39si77Hlo6DAm-EMKcGUDorti25HGabCONiR8NZoUBVeB3msV5l7hYvrwM_Q0xwICtRD-uXAw3pYhJQ50ow69LRRJkAkZpcQ'
    yt_service.client_id = 'youtube_uploader'
    try :
        yt_service.ProgrammaticLogin()
    except :
        raise 'Could not authenticate user'
        return 0
    
    # prepare a media group object to hold our video's meta-data
    my_media_group = gdata.media.Group(
    title=gdata.media.Title(text=video_title),
    description=gdata.media.Description(description_type='plain',
                                      text='Uploaded from EasyShare'),
    keywords=gdata.media.Keywords(text='EasyShare'),
    category=[gdata.media.Category(
      text='Autos',
      scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
      label='Autos')],
      player=None
    )
    try:    
        video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group,geo=None)
        video_location = filename
        try :
            new_entry = yt_service.InsertVideoEntry(video_entry, video_location)
        except :
            raise 'Error uploading video'
            return 0
        try :
            res = re.search("href=\"(.*?)\"",str(new_entry.GetHtmlLink()),0)
            if res.group(1) is not None:
                return res.group(1)
            else:
                return 0
        except : 
            raise 'Error in reg ex'
            return 0
    
    except:
        raise "Error with uploading"
        return 0
        
#print post_to_youtube('/home/pali/Downloads/test.mp4','OpenHackIndia', username='kartalkhan', password='kartalkhanAjja')