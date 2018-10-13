from instapy import InstaPy
insta_username = 'stal_style'
insta_password = 'Dylan9790'

bot = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
bot.login()
bot.set_relationship_bounds(enabled=True,
  potency_ratio=-1.21,
  delimit_by_numbers=True,
  min_followers=40,
  min_following=40)
bot.like_by_tags([
    pink,
    underwear,
    instadaily,
    picoftheday,
    instapic,
    instagood,
    glamour,
    style,
    mood,
    newyorkcity,
    fashion,
    love,
    beautiful,
    happy,
    women,
    empower
], amount=100)
bot.end()