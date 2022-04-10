from django.urls import path

from .views import JogoViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('jogos', JogoViewSet)


'''
urlpatterns = [ 
    path('jogos/', JogosAPIView.as_view(), name='jogos'),
    path('jogos/<int:pk>/', JogoAPIView.as_view(), name='jogo')    
]

'''