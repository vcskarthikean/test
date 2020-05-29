import tweepy

#below token is removed for security purpose.
#need to add when the actual developer token is generated
auth = tweepy.OAuthHandler("token", "token_key")
auth.set_access_token("token", "key")

api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)



