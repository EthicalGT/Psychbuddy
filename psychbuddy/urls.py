#from django.contrib import admin
from django.urls import path
from psychbuddy import views

urlpatterns = [
    path('admin/', views.admindashboard),
    path('', views.index, name='index'),
    path('first', views.email, name='email'),
    path('second', views.OTP, name='otp'),
    path('third', views.otpVerify, name='verify'),
    path('signedUp',views.signupUser, name='signup'),
    path('signin',views.signin,name='signin'),
    path('homepage',views.homePage, name='homepage'),
    path('GIA',views.GIA,name='GIA'),
    path('myforum',views.forum),
    path('news',views.news_view),
    path('forum',views.chatForum, name='chatforum'),
    path('sessions',views.sessions),
    path('individualtherapy',views.individual_therapy),
    path('grouptherapy',views.group_therapy),
    path('heartbrokentherapy',views.heartbroken_therapy),
    path('traumatherapy',views.trauma_therapy),
    path('coupletherapy',views.couple_therapy),
    path('familytherapy',views.family_therapy),
    path('psychiatrist',views.psychiatrist),
    path('psychinfo',views.psych_info),
    path('relaxation',views.audio_therapy),
    path('wellnessLog',views.wellnessLog),
    path('wellnesslogdir',views.wellnessLogDir),
    path('wellnessLogFileCreator',views.wellnessLogFileCreator),
    path('YM',views.YandM),
    path('tips',views.tips),
    path('adminlogin',views.adminLogin),
    path('emotion_detection/',views.emotion_detection),
    path('feedback',views.feedback),
    path('books',views.books),
    path('whatsapp',views.whatsapp),
    path('instagram',views.instagram),
    path('facebook',views.facebook),
    path('aboutus',views.aboutus),
    path('admin/usersNav',views.usersNav),
    path('admin/manageResources',views.manageResources),
    path('admin/videoRes',views.videoResourcesUpload),
    path('admin/audioRes',views.audioResourcesUpload),
    path('admin/yRes',views.yResourcesUpload),
    path('admin/mRes',views.mResourcesUpload),
    path('admin/bookRes',views.bookResourcesUpload),
    path('admin/delYRes', views.deleteYoga),
    path('admin/delMRes', views.deleteMeditation),
    path('admin/delBook',views.deleteBookResource),
    path('admin/delAudio',views.deleteAudioResource),
    path('admin/delVideoSessions',views.deleteVideoResource),
    path('admin/adminforum',views.chatAdminForum),
    path('admin/feedbackinfo',views.feedbackinfo),
    path('admin/appointmentmail',views.fixappointmentmail),
    path('admin/admintips',views.admintips),
    path('admin/adminlogout',views.adminlogout),
]