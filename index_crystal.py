from instapy import InstaPy
# Config
insta_username = 'stal_style'
insta_password = 'Dylan9790'

# Setup
session = InstaPy(username=insta_username, password=insta_password, nogui=True)
session.login()
# Like Posts
session.like_by_tags(['styledbystal', 'style', 'stylist', 'ootd', 'fashion', 'nycstylist', 'nycstyle', 'lookbook', 'fashiongram', 'wiwt', 'lookoftheday', 'stylish', 'streetstyle', 'instastyle', 'styleinspiration', 'empower', 'women', 'instafashion', 'fashionblogger', 'fashionista', 'streetstyle', 'stylish', 'mensfashion', 'instastyle', 'lookbook', 'whatiwore', 'styleinspo', 'styleblogger'], amount=100)
# end the bot session
session.end()
