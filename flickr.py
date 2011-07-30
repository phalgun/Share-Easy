import flickrapi
from flickrapi import shorturl
flickr_consumer_key = '15db702bed17c8a506386f702f52ece9'
flickr_consumer_secret = '1ffd4e31c13efcf8'
flickr_token = None
photo_url = None

def func(progress, done):
    if done:
        return 'success'
    else:
        return 'Error in network connection'
'''
    It takes a the filename and title of the photo
    uploads the photo onto flickr
    and returns a shortened url of the same
'''

def post_to_flickr(file,title):
    try :
        flickr = flickrapi.FlickrAPI(flickr_consumer_key, flickr_consumer_secret)
    except :
        return 'Error in app consumer key'
    try :
        (token, frob) = flickr.get_token_part_one(perms='write')
    except :
        return 'Error in authenticating user'
    
    if not token: raw_input("Press ENTER after you authorized this program")
    try :
        flickr.get_token_part_two((token, frob))
        flickr_token = token
    except :
        return 'Error in authorizing'
    try :
        resp = flickr.upload(filename=file, callback=func, title=title)
        photoid = resp.find('photoid').text
        photourl = shorturl.url(photoid)
        return photourl
    except :
        return 'Error uploading'

#post_to_flickr('/home/pali/Downloads/flickr-yahoo-logo.png.jpg', 'flickr')