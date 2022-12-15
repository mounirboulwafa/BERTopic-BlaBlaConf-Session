import tweepy
import json

# Set the path to your credentials JSON file:
credentials = "Twitter-API-Keys.json"
with open(credentials, "r") as keys:
    api_tokens = json.load(keys)

# Grab the API keys:
API_KEY = api_tokens["api_key"]
API_SECRET = api_tokens["api_secret"]
BEARER_TOKEN = api_tokens["bearer_token"]
ACCESS_TOKEN = api_tokens["access_token"]
ACCESS_SECRET = api_tokens["access_secret"]

# We use Tweepy's OAuthHandler method to authenticate our credentials:
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)

# Then, we set our access tokens by calling the auth object directly:
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Finally, we can initialize the Twitter API. 
# NOTE: we will be using this `api` object to interact
# with Twitter from here on out:
api = tweepy.API(auth, wait_on_rate_limit=True)


for user in tweepy.Cursor(api.get_followers, screen_name="geeksblabla").items():
    # Get Followers objects as Json :
    # print(user._json)

    with open('followers copy.json', 'a') as followers_file:
        followers_file.write(json.dumps(user._json) + '\n')

    # follower = {
    #     'screen_name': user.screen_name,
    #     'id': user.id,
    #     'name': user.name,
    #     'description': user.description,
    #     'location':user.location,
    #     'url':user.url,
    # }

    # print('follower: ' + user.screen_name)