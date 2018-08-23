from instapy import InstaPy
import schedule
import time

def job():
    try:
        insta_username = 'schoennyc'
        insta_password = 'theman'
        smartTags = ['a7sii', 'a7s', 'rokinon', 'sonyalpha', 'atomos', 'film', '35mm']
        bot = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
        bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
        bot.login()
        bot.set_smart_hashtags(smartTags, limit=3, sort='top', log_tags=True)
        bot.like_by_tags(amount=random.randint(2,5), use_smart_hashtags=True)
        bot.end()
    except:
        import traceback
        print(traceback.format_exc())
        
schedule.every().day.at("9:00").do(job)
schedule.every().day.at("21:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)