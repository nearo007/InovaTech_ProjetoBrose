
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para a administração do Django
    path('', views.minha_view, name='index'),  # Mapeia a URL raiz para a view minha_view
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),  # URL para login
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_new.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_changed.html"), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para logout
    path('register/', views.register, name='register'),  # URL para registro de novos usuários
    path('main/', views.lista_funcionarios, name='main'),  # Corrigido para lista_funcionarios
    path('adicionar_funcionario/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('remove_funcionario/<int:funcionario_id>/', views.remove_funcionario, name='remove_funcionario'),
    path('funcionario/<int:funcionario_id>/', views.funcionario_detalhes, name='funcionario_detail'),  # Corrigido para nome correto da URL)
    path('funcionario/<int:funcionario_id>/add_skill/', views.add_skill, name='add_skill'),  # Adiciona skill ao funcionário
    path('comparar_funcionario_skills/<int:funcionario_id>/', views.comparar_funcionario_skills, name='comparar_funcionario_skills'),
    path('relatorio/', views.relatorio_dinamico, name='relatorio_dinamico'),
    path('calendario/eventos/', views.calendario_eventos, name='calendario_eventos'),
    path('calendario/', views.calendarioView, name='calendario'),
    path('calendario/adicionar/', views.adicionar_item_view, name='adicionar_item'),
    path('calendario/deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),
    path('relatorio/pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
    path('editar_cargos/', views.editar_cargos, name='editar_cargos'),
    path('adicionar_cargo/', views.adicionar_cargo, name='editar_cargos'),
    path('remove_cargo/<int:cargo_id>/', views.remove_cargo, name='remove_cargo'),
    path('editar_skills/', views.adicionar_skill, name='editar_skills'),
    path('remove_skill/<int:skill_id>/', views.remove_skill, name='remove_skill'),
]
