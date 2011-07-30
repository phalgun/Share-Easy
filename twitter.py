import webbrowser
import tweepy
from compiler.ast import Raise

twitter_consumer_key = 'kqufl3IFwW9Fa9ZX2CoqIQ'
twitter_consumer_secret = 'T1nzYDExfdh6oPUdT4F0rmClvCWFt9U2Ft6KI9ytAM'
twitter_oauth_key = None
twitter_oauth_secret = None

"""
    Query the user for their consumer key/secret
    then attempt to fetch a valid access token.
"""

def post_to_twitter(link):

    auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    # Open authorization URL in browser
    try :
        webbrowser.open(auth.get_authorization_url())
    except :
        return 'Could not open browser'

    # Ask user for verifier pin
    # Call UI here
    pin = raw_input('Enter the Verification pin number from twitter.com: ').strip()

    # Get access token
    try :
        token = auth.get_access_token(verifier=pin)
    except :
        return 'Authorization error'

    twitter_oauth_key = token.key
    twitter_oauth_secret = token.secret
    try :
        auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(twitter_oauth_key, twitter_oauth_secret)
    except : 
        return 'Could not authorize user'
    
    twit_user = tweepy.API()
    
    try :
        api = tweepy.API(auth)
        api.update_status(link+" via ShareEasy #openhackindia")
    except :
        return 'Error in connecting to the network'

    return 'success'

#post_to_twitter(link = 'Twitter api - conquered!')
