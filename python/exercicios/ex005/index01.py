import emoji
from django.templatetags.i18n import language

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is fun :red_heart:', language='pt'))
