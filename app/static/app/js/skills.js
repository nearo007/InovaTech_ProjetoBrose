// Função para adicionar uma skill
function addSkill() {
    var skillInput = document.getElementById('skillInput');
    var skillValue = skillInput.value.trim();

    if (skillValue === '') {
        alert('Por favor, digite uma skill.');
        return;
    }

    var li = document.createElement('li');
    li.textContent = skillValue;

    var ul = document.getElementById('skillsUl');
    ul.appendChild(li);

    skillInput.value = ''; // Limpa o campo de input
}

$(document).ready(function() {
    $('#skillForm').on('submit', function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(), // Serializa os dados do formulário
            success: function(response) {
                // Atualiza a lista de skills com o HTML retornado
                $('#skillsUl').html(response.skills_html);
            },
            error: function(xhr, status, error) {
                console.error('Erro ao adicionar skill:', error);
            }
        });
    });

    $('#skillsUl').on('click', '.remove-skill', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        var url = $(this).attr('href'); // Obtém a URL do link

        $.ajax({
            type: 'GET', // Ou 'POST' se você preferir
            url: url,
            success: function(response) {
                // Atualiza a lista de skills com o HTML retornado
                $('#skillsUl').html(response.skills_html);
            },
            error: function(xhr, status, error) {
                console.error('Erro ao remover skill:', error);
            }
        });
    });
});
