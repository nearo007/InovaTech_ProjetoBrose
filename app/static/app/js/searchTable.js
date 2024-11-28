function filterTable() {
    // Obtém o valor da barra de pesquisa
    var input = document.getElementById("searchInput");
    var filter = input.value.toLowerCase();
    var table = document.getElementsByTagName("table")[0];
    var tr = table.getElementsByTagName("tr");

    // Itera sobre todas as linhas da tabela (ignorando a primeira linha com o cabeçalho)
    for (var i = 1; i < tr.length; i++) {
        var td = tr[i].getElementsByTagName("td")[0]; // Obtém a primeira célula (nome do funcionário)
        if (td) {
            var txtValue = td.textContent || td.innerText;
            // Verifica se o valor da célula começa com o filtro digitado
            if (txtValue.toLowerCase().startsWith(filter)) {
                tr[i].style.display = ""; // Mostra a linha se corresponder ao filtro
            } else {
                tr[i].style.display = "none"; // Oculta a linha se não corresponder ao filtro
            }
        }
    }
}