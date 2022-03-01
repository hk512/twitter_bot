import json

with open('settings.json', 'r') as f:
    json_data = json.load(f)

consumer_key = json_data['twitter']['consumer_key']
consumer_secret = json_data['twitter']['consumer_secret']
access_token = json_data['twitter']['access_token']
access_token_secret = json_data['twitter']['access_token_secret']

interval_min = json_data['bot']['interval_min']

favorite_enable = json_data['bot']['favorite']['enable']
favorite_max_count = json_data['bot']['favorite']['max_count']
favorite_words = json_data['bot']['favorite']['words']

create_friendships_enable = json_data['bot']['create_friendships']['enable']
create_friendships_max_count = json_data['bot']['create_friendships']['max_count']

destroy_friendships_enable = json_data['bot']['destroy_friendships']['enable']
destroy_friendships_max_count = json_data['bot']['destroy_friendships']['max_count']
