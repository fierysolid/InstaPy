import random 
from instapy import InstaPy
import os
import multiprocessing
import datetime
import time

instaUser = ['schoennyc']#, 'stal_style']
instaPass = ['theman']#, 'Dylan9790']
smartTags = [['a7sii', 'a7s', 'rokinon', 'sonyalpha', 'atomos', 'film', '35mm'], ['styledbystal', 'style', 'stylist', 'ootd', 'fashion', 'nycstylist', 'nycstyle', 'lookbook', 'fashiongram', 'wiwt', 'lookoftheday', 'stylish', 'streetstyle', 'instastyle', 'styleinspiration', 'empower', 'women', 'instafashion', 'fashionblogger', 'fashionista', 'streetstyle', 'stylish', 'mensfashion', 'instastyle', 'lookbook', 'whatiwore', 'styleinspo', 'styleblogger']]

def worker(selection):
    
    print("MULTI - Started as",instaUser[selection],"at",datetime.datetime.now().strftime("%H:%M:%S"))
    session = InstaPy(username=instaUser[selection], password=instaPass[selection], selenium_local_session=False)
    session.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
    session.login()
   
    if smartTags[selection]:
        session.set_smart_hashtags(smartTags[selection], limit=3, sort='top', log_tags=True)
        session.like_by_tags(amount=random.randint(2,5), use_smart_hashtags=True)
        print("MULTI -",instaUser[selection],"finished smartTags at",datetime.datetime.now().strftime("%H:%M:%S"))

    session.end()
    print("MULTI -",instaUser[selection],"finished run at",datetime.datetime.now().strftime("%H:%M:%S"))

if __name__ == '__main__':        
    print("MULTI -","Starting at",datetime.datetime.now().strftime("%H:%M:%S"))
    jobs = []
    for i in range(len(instaUser)):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
        time.sleep(66);#no delay cause some instances of chrome to give errors and stop