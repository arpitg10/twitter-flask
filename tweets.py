from dao import get_twitter_response


def tweets_by_hashtag(hashtag, pageSize):
    endpoint = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': f'#{hashtag}', 'tweet.fields': 'author_id,created_at,public_metrics',
                    'max_results': pageSize}

    return get_twitter_response(endpoint, query_params)['data']


def get_user_tweets(user_id, pageSize):
    endpoint = f"https://api.twitter.com/2/users/{user_id}/tweets"
    query_params = {'tweet.fields': 'author_id,created_at,public_metrics', 'max_results': pageSize}

    return get_twitter_response(endpoint, query_params)['data']
