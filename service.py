from accounts import get_twitter_account, get_twitter_account_by_username
from tweets import tweets_by_hashtag, get_user_tweets


def get_tweets_by_hashtag(hashtag, pageSize):
    tweets = tweets_by_hashtag(hashtag, pageSize)
    return [response_builder(tweet, get_twitter_account(tweet['author_id'])) for tweet in tweets]


def get_user_tweets_by_user(username, pageSize):
    account = get_twitter_account_by_username(username)
    tweets = get_user_tweets(account['id'], pageSize)

    return [response_builder(tweet, account) for tweet in tweets]


def response_builder(tweet, account):
    return {
        'account': {
            'fullname': account['name'],
            'href': f"/{account['username']}",
            'id': account['id']
        },
        'date': tweet['created_at'],
        'hashtags': [x for x in tweet['text'].split() if x.startswith('#')],
        'likes': tweet['public_metrics']['like_count'],
        'replies': tweet['public_metrics']['reply_count'],
        'retweets': tweet['public_metrics']['retweet_count'],
        'text': tweet['text']
    }
