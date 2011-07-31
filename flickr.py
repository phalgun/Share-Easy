import flickrapi
import globals
from flickrapi import shorturl

flickr_consumer_key = '15db702bed17c8a506386f702f52ece9'
flickr_consumer_secret = '1ffd4e31c13efcf8'
token = None
photo_url = None

def func(progress, done):
    if done:
        return 1
    else:
        raise 'Slow network connection,please wait'
'''
    It takes a the filename and title of the photo
    uploads the photo onto flickr
    and returns a shortened url of the same
'''

def post_to_flickr(file,title):
    try :
        flickr = flickrapi.FlickrAPI(flickr_consumer_key, flickr_consumer_secret)
    except :
        raise 'Error in app consumer key'
        return 0
    token = globals.flickr_token 
    if token is None :
        try : 
            (token, frob) = flickr.get_token_part_one(perms='write')
        except :
            raise 'Error in authenticating user'
            return 0

    #UI comes into picture here
    # Change this to some OK button or so..
    if not token: raw_input("Press ENTER after you authorized this program")
    try :
        flickr.get_token_part_two((token, frob))
        globals.flickr_token = token
    except :
        raise 'Error in authorizing'
        return 0
    
    try :
        resp = flickr.upload(filename=file, callback=func, title=title)
        photoid = resp.find('photoid').text
        photourl = shorturl.url(photoid)
        return photourl
    except :
        raise 'Error uploading'
        return 0

#post_to_flickr('/home/pali/Downloads/flickr-yahoo-logo.png.jpg', 'flickr')