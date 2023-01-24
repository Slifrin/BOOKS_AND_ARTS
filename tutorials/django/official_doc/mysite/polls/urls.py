from django.urls import path

from polls import views


app_name = 'polls'
urlpatterns = [
    # ex:  /polls/
    path('', views.index, name="index"),
    # ex: /polls/alt/
    path('alt/', views.index2, name="index_2"),
    # ex: /pools/5/
    # path('specific/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /pools/alt/5/
    path('alt/<int:question_id>/', views.detail_alternative, name='detail2'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]