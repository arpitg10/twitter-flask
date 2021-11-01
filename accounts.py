from dao import get_twitter_response


def get_twitter_account(account_id):
    endpoint = f"https://api.twitter.com/2/users/{account_id}"

    return get_twitter_response(endpoint)['data']


def get_twitter_account_by_username(username):
    endpoint = f"https://api.twitter.com/2/users/by/username/{username}"

    return get_twitter_response(endpoint)['data']
