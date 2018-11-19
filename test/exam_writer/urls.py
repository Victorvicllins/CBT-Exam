from django.urls import path
from . import views

app_name = "exam_writer"

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
]