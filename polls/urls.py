from django.urls import path
from . import views


app_name = 'polls'  # view의 이름이 다른 앱과 겹칠 것을 대비하여 앱 이름공간 설
urlpatterns = [
    # /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path(route, view, kwargs, name)
    # 1. route: 경로
    # config.urls에서 1차 처리한 후 남은 경로가 polls.urls로 전달
    # -> 경로가 비었다면 뷰가 처리
    # 2. kwargs: 뷰에 전달할 키워드 인자
    # 3. name: route에 부여하는 이름

    # /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /polls/5/result/
    # path('<int:question_id>/result', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]