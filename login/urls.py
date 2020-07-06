from django.urls import path
from . import views
from . import static
urlpatterns = [
    path('', views.splash, name='splash'),
    path('login',views.login,name="login"),
    path('forgot',views.forgot,name="forgot"),
    path('question',views.question,name="question"),
    path('topic',views.topic,name="topic"),
    path('end',views.end,name="end")
]