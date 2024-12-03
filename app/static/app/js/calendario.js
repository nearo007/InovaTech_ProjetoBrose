document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendario');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: function(fetchInfo, successCallback, failureCallback) {
            fetch('/calendario/eventos/')
                .then(response => response.json())
                .then(events => {
                    // Adicionar 1 dia à data final de cada evento
                    events.forEach(event => {
                        if (event.end) {
                            let endDate = new Date(event.end);
                            endDate.setDate(endDate.getDate() + 1); // Adiciona 1 dia
                            event.end = endDate.toISOString(); // Converte de volta para ISO 8601
                        }
                    });
                    successCallback(events);
                })
                .catch(error => failureCallback(error));
        },
        eventClick: function(info) {
            var url = `/calendario/deletar/${info.event.id}/`;
            console.log('URL da exclusão:', url);
            if (confirm('Tem certeza de que deseja excluir este evento?')) {
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    })
                }).then(response => {
                    console.log('Resposta da exclusão:', response);
                    if (response.ok) {
                        info.event.remove();
                    } else {
                        return response.text().then(text => { throw new Error(text); });
                    }
                }).catch(error => {
                    console.error('Erro ao excluir o evento:', error);
                    alert('Erro ao excluir o evento.');
                });
            }
        }
    });

    calendar.render();

    document.getElementById('event-form').addEventListener('submit', function(e) {
        e.preventDefault();

        var formData = new FormData(this);

        fetch(this.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        }).then(response => {
            if (response.ok) {
                return response.text();
            }
            throw new Error('Network response was not ok.');
        }).then(() => {
            calendar.refetchEvents();
            this.reset();
        }).catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    });
});
