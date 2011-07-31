#!/usr/bin/python

###
# This script serves to upload the pictures from the specified directory to the specified album in picasa.
# Usage : python picasaUploader -l <source directory> 
###
import gdata.photos.service
import gdata.media
import gdata.geo
import re

'''
    Function takes in filename,title,username and password
    uploads the given photo to the account
    and returns the url of that photo
'''
def post_to_picasa(filename,photo_title,username,password):
    
    gd_client = gdata.photos.service.PhotosService()
    #UI should be called and parameters passed!
    gd_client.email = username #type your username here
    gd_client.password = password # store your password in an environment variable called PASSWD
    gd_client.source = 'python uploader'
    try:
        gd_client.ProgrammaticLogin()
    except:
        raise 'Could not authenticate the user'
        return 0
    
    username=gd_client.email
    index = 0
    try:
        album = gd_client.InsertAlbum(title=photo_title, summary='Uploaded from EasyShare')
    except:
        raise 'Could not create Album'
        return 0
    album_url = '/data/feed/api/user/%s/albumid/%s' %(username,album.gphoto_id.text)
    try:
        photo = gd_client.InsertPhotoSimple(album_url,photo_title,'Uploaded from EasyShare',filename,content_type='image/jpeg')
    except :
        raise 'Error uploading photo'
        return 0
    try:
        res = re.search("href=\"(.*?)\"",str(photo.GetHtmlLink()),0)
        if res.group(1) is not None:
            return res.group(1)
        else:
            raise 'Could not extract link'
            return 0
    except: 
        raise 'Error in reg ex'
        return 0

#print post_to_picasa(filename = '/home/pali/Pictures/ubu.jpg', photo_title='Ubuntu', username = 'kartalkhan', password = 'kartalkhanAjja')