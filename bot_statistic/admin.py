from lemon import extradmin
from bot_statistic.models import LogItem


extradmin.site.register(LogItem)
