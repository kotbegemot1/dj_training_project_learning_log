"""определяет схумы  URL для learning_logs"""

from django.conf.urls import url 

from . import views 

urlpatterns = [
	# домашняя страница 
	url(r'^$', views.index, name='index'),

	# вывод всех тем
	url(r'^topics/$', views.topics, name='topics'),

	# # страница с подробной информацией по отдельной теме
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# страница для добавления новой темы
	url(r'new_topic$', views.new_topic, name='new_topic'),
	
	# страница для добавления новой записи
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# страница для редактирования записей
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]