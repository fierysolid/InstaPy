from instapy import InstaPy
import schedule
import time

insta_username = 'dylan_underwear'
insta_password = 'Dylan9790'

def job():
    try:
        session = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
        session.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
        session.login()
        session.set_relationship_bounds(enabled=True,
          potency_ratio=-1.21,
          delimit_by_numbers=True,
          max_followers=4590,
          max_following=5555,
          min_followers=45,
          min_following=77)
        session.like_by_tags([
            'pink',
            'underwear',
            'instadaily',
            'picoftheday',
            'instapic',
            'instagood',
            'glamour',
            'style',
            'mood',
            'newyorkcity',
            'fashion',
            'love',
            'beautiful',
            'happy',
            'women',
            'empower'
        ], amount=100)
        session.end()
    except:
        import traceback
        print(traceback.format_exc())

def main():
    time.sleep(30)
    job()

if __name__ == "__main__":
    main()
# schedule.every().day.at("6:35").do(job)
# schedule.every().day.at("16:22").do(job)
# 
# while True:
#     schedule.run_pending()
#     time.sleep(1)