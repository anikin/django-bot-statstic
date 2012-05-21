from django.conf.urls.defaults import patterns, url

from bot_statistic.models import LogItem
from bot_statistic.views import LogItemListView


urlpatterns = patterns('catalog.views',
    url(r'^$', LogItemListView.as_view(
            model=LogItem,
            template_name='admin/bot_statistic/logitem/change_list.html',
        ),
        name='bot_statistic_logitem_list'),
)
