from django.contrib import admin
from .models import Funcionario, CalendarioItem, Skill, Cargo

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'data_nascimento')

@admin.register(CalendarioItem)
class CalendarioItemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'data_fim', 'descricao')

    def delete_selected(self, request, queryset):
        # Adiciona uma ação personalizada para excluir os eventos selecionados
        num_deleted, _ = queryset.delete()
        self.message_user(request, f'{num_deleted} evento(s) excluído(s).')
    delete_selected.short_description = 'Excluir eventos selecionados'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')

    def delete_selected(self, request, queryset):
        # Adiciona uma ação personalizada para excluir os eventos selecionados
        num_deleted, _ = queryset.delete()
        self.message_user(request, f'{num_deleted} evento(s) excluído(s).')
    delete_selected.short_description = 'Excluir eventos selecionados'

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'display_skills')

    def display_skills(self, obj):
        return ", ".join([skill.nome for skill in obj.skills.all()])

    def delete_selected(self, request, queryset):
        # Adiciona uma ação personalizada para excluir os eventos selecionados
        num_deleted, _ = queryset.delete()
        self.message_user(request, f'{num_deleted} evento(s) excluído(s).')
    delete_selected.short_description = 'Excluir eventos selecionados'