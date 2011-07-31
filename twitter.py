import webbrowser
import tweepy
from compiler.ast import Raise
import globals
twitter_consumer_key = 'kqufl3IFwW9Fa9ZX2CoqIQ'
twitter_consumer_secret = 'T1nzYDExfdh6oPUdT4F0rmClvCWFt9U2Ft6KI9ytAM'

"""
    Query the user for their consumer key/secret
    then attempt to fetch a valid access token.
"""

def post_to_twitter(link):

    auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    # Open authorization URL in browser
    if globals.twitter_oauth_key is None or globals.twitter_oauth_secret is None :
        try :
            webbrowser.open(auth.get_authorization_url())
        except :
            raise 'Could not open browser'
            return 0
        
        # Ask user for verifier pin
        # Call UI here
        pin = raw_input('Enter the Verification pin number from twitter.com: ').strip()
    
        # Get access token
        try :
            token = auth.get_access_token(verifier=pin)
        except :
            raise 'Authorization error'
            return 0
    
        globals.twitter_oauth_key = token.key
        globals.twitter_oauth_secret = token.secret
    else :
        twitter_oauth_key = globals.twitter_oauth_key
        twitter_oauth_secret = globals.twitter_oauth_secret
        
    try :
        auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(globals.twitter_oauth_key, globals.twitter_oauth_secret)
    except : 
        raise 'Could not authorize user'
        return 0
    twit_user = tweepy.API()
    
    try :
        api = tweepy.API(auth)
        api.update_status(link+" via ShareEasy #openhackindia")
    except :
        raise 'Error in connecting to the network'
        return 0

    return 1

#post_to_twitter(link = 'Last minute fumbles')
