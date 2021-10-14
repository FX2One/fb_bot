from facebook_bot.fb_bot import Fb_bot
import json

if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    driver = config['driver']
    url = config['url']
    username = config['username']
    password = config['password']

    Fb_bot(driver,url,username,password)
