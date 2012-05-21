from django.views.generic import ListView
from bot_statistic.models import LogItem


class LogItemListView(ListView):

    def get_context_data(self, **kwargs):
        yandex_list = LogItem.objects.filter(bot='y')
        google_list = LogItem.objects.filter(bot='g')
        return {'yandex_list': yandex_list,
                'google_list': google_list}