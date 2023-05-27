from django.urls import path
from . import views

urlpatterns = [
    path('', views.voos_view, name='voos'),
    path('voo/<int:voo_id>', views.voo_view, name='voo'),
    path('adicionar/<int:voo_id>', views.adicionar_passageiro_view, name='adicionar'),
    path('remover/<int:voo_id>/<int:passageiro_id>', views.remover_passageiro_view, name='remover'),

    path('passageiros', views.passageiros_view, name='passageiros'),
    path('passageiro/<int:passageiro_id>', views.passageiro_view, name='passageiro'),

    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]