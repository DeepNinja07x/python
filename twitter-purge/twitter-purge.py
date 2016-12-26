from datetime import datetime, timedelta
import tweepy
import config


def process():
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.TOKEN, config.TOKEN_SECRET)
    # http://docs.tweepy.org/en/v3.5.0/api.html
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    user = api.me()
    tweets = fetch_tweets(api, user.screen_name)
    purge_old_tweets(api, tweets)


def fetch_tweets(api, user_screen_name):
    return api.user_timeline(screen_name=user_screen_name, count=100, include_rts=True)


def purge_old_tweets(api, tweets):
    max_keep_date = datetime.today() + timedelta(-config.DAYS_TO_KEEP)
    for tweet in tweets:
        if tweet.created_at < max_keep_date:
            api.destroy_status(tweet.id)
            print(".", end="")
    print("FINISHED")


if __name__ == "__main__":
    process()
