from django.urls import path, re_path
from . import views
app_name = "examination"

urlpatterns = [
	path('', views.home_view, name="index"),
	#re_path(r'^user/(?P<public_key>\d{0,50})/$', views.examView, name='ativated-exam'),
    path('userresult/', views.userResult, name='ativated-exam'),
    path('exam/<int:id>/', views.index_view, name="exam-home"),
    path('qprepare/', views.questionFile, name="uploads"),
    path('crateSubject/', views.subjectCreate, name="subUploads"),
    path('csvuploader/', views.questionCsvUpload, name="csvUploads"),
    path('my_pdf/', views.GeneratePDF.as_view(), name="result"),
]
