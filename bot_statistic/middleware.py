from bot_statistic.models import LogItem
from datetime import datetime


class BotStatisticMiddleware(object):

    def process_request(self, request):

        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']

            if user_agent == 'Mozilla/5.0 (compatible; YandexBot/3.0)':
                log = LogItem()
                log.bot = 'y'
                log.log_date = datetime.now()
                log.url = request.path
                log.save()
            elif user_agent == 'Googlebot/2.1 (+http://www.google.com/bot.html)':
                log = LogItem()
                log.bot = 'g'
                log.log_date = datetime.now()
                log.url = request.path
                log.save()
            else:
                pass