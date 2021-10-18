import json
import random
from facebook_bot.fb_bot_reg import Fb_bot_register

if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    driver = config['driver']
    url = config['url']

    #open file with list of first names
    #pick randomly one first name out of given json file
    with open('name.json') as file:
        config = json.load(file)

        def random_name(conf_file: list[str]):
            for i in range(1):
                name = random.choice(conf_file)
            return name

    firstName: str = random_name(config)
    print(firstName)

    #open file with list of last names
    #pick randomly one last name out of given json file
    with open('lastname.json') as lfile:
        lconfig = json.load(lfile)

        def random_lname(conf_file: list[str]):
            for i in range(1):
                lname = random.choice(conf_file)
            return lname

    lastName: str = random_lname(lconfig)
    print(lastName)

    rand_num = (random.randrange(100, 1000, 3))

    randMail = f'{firstName}_{rand_num}_{lastName}@gmail.com'

    Fb_bot_register(driver,url,firstName,lastName,randMail)





