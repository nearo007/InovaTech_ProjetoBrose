from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CalendarioItem, Funcionario, Skill, Cargo

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username', 'placeholder': 'Digite seu nome de usuário'}),
    label='Nome de usuário'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email', 'placeholder': 'Digite seu email'}),
        label='Email'
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password', 'placeholder': 'Crie uma senha'}),
        help_text='Coloque sua senha.'
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password2', 'placeholder': 'Confirme sua senha'}),
        help_text='Coloque a mesma senha.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Nome de usuário ja existe.')
        
        elif ' ' in username:
            raise ValidationError('Nome de usuário não pode conter espaços.')

        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email ja cadastrado.')
        
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("As senhas não são iguais.")
            
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username'}),
        label='Nome de usuário'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password'}),
        label='Senha'
    )

class FuncionarioForm(forms.ModelForm):
    gestor = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Funcionario
        fields = ['nome', 'data_nascimento', 'cargo', 'gestor']

    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/aaaa'})
    )

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['nome', 'nivel']

class CargoForm(forms.ModelForm):    
    skills = forms.ModelMultipleChoiceField(
    queryset=Skill.objects.all(),  # Carrega todas as habilidades
    widget=forms.CheckboxSelectMultiple,  # Ou use outro widget de sua escolha
    required=False  # Define se a seleção de skills é obrigatória
    )
    
    class Meta:
        model = Cargo
        fields = ['nome', 'skills']

class FindCargoForm(forms.Form):
    cargo_promover = forms.ModelChoiceField(
        queryset=Cargo.objects.all(),
        label="Selecione o cargo para comparar",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class CalendarioItemForm(forms.ModelForm):
    class Meta:
        model = CalendarioItem
        fields = ['data_inicio', 'data_fim', 'titulo', 'descricao']