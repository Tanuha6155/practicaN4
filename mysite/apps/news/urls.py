from django.urls import path
from .views import PostsList, PostDetail
# from .views import Init

urlpatterns = [
        path('', PostsList.as_view()),
        path('<int:pk>', PostDetail.as_view()),
        # path('/init', Init.as_view()),
    ]
