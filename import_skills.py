import os
import django
import json
# Defina o módulo de configurações
os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto.settings'

# Configure o Django
django.setup()

from app.models import Skill  # Substitua "myapp" pelo nome do seu app
from django.core.exceptions import ValidationError

# Exemplo de dados JSON
with open('skills.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)
# Carregar os dados JSON
skills_data = json_data

# Inserir os dados no banco de dados
for skill_data in skills_data:
    try:
        skill, created = Skill.objects.get_or_create(
            nome=skill_data['nome'],
            defaults={'nivel': skill_data['nivel']}
        )
        
        if created:
            print(f"Skill '{skill.nome}' adicionada com nível {skill.nivel}.")
        else:
            print(f"A skill '{skill.nome}' já existe no banco de dados.")
    except ValidationError as e:
        print(f"Erro de validação ao adicionar '{skill_data['nome']}': {e}")
