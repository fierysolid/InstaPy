from instapy import InstaPy
insta_username = 'schoennyc'
insta_password = 'theman'

bot = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
bot.login()
bot.set_relationship_bounds(enabled=True,
  potency_ratio=-1.21,
  delimit_by_numbers=True,
  min_followers=40,
  min_following=40)
bot.like_by_tags(['a7sii',
    'a7s',
    'rokinon',
    'sonyalpha',
    'atomos',
    'film',
    '35mm',
    'film',
    'filmphotographyfilmisnotdead',
    '35mm',
    'analog',
    'movie',
    'ishootfilm',
    'cinema',
    'filmcamera',
    'believeinfilm',
    'filmcommunity',
    'analogue',
    'kodak',
    'analogphotography',
    'staybrokeshootfilm',
    'filmfeed',
    'movies',
    'buyfilmnotmegapixels',
    'thefilmcommunity',
    'shootfilm',
    'socialdraft',
    '35mmfilm',
    'filmmaking',
    'actor ',
    'keepfilmalive',
    'filmphoto',
    'films',
    'filmmaker',
    'mediumformat'], amount=100)
bot.end()