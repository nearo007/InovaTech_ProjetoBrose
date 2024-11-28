let lastSortedColumn = -1;  // Armazena a última coluna clicada, começa por um valor inesistente (-1)
let isAscending = true;     // Armazena a direção da ordenação

function sortTable(column) {
    let table = document.getElementById('funcionariosTabela');
    let rows = Array.from(table.rows).slice(1);

    // Se for uma nova coluna, comece sempre ascendente
    if (column !== lastSortedColumn) { // Na primeira vez sempre será true
        isAscending = true;
    }
    
    else {
        // Se clicar na mesma coluna, inverte a direção
        isAscending = !isAscending;
    }

    lastSortedColumn = column;  // Atualiza a última coluna clicada

    // Reset the headers for all columns before sorting
    document.querySelectorAll('th').forEach(function (th) {
        th.innerHTML = th.innerHTML.replace(' ▼', '').replace(' ▲', '');
    });

    rows.sort(function (rowA, rowB) {
        let cellA = rowA.cells[column].textContent.trim();
        let cellB = rowB.cells[column].textContent.trim();

        if (column === 2) {
            let dateA = cellA.split("/").reverse().join("-");
            let dateB = cellB.split("/").reverse().join("-");

            if (isAscending) {
                return new Date(dateA) - new Date(dateB);
            } else {
                return new Date(dateB) - new Date(dateA);
            }
        }

        let valA = isNaN(cellA) ? cellA : Number(cellA);
        let valB = isNaN(cellB) ? cellB : Number(cellB);

        if (isAscending) {
            if (valA > valB) {
                return 1;
            } else {
                return -1;
            }
        }
        
        else {
            if (valA < valB) {
                return 1;
            } else {
                return -1;
            }
        }
    });

    // Atualiza o cabeçalho após a ordenação
    if (isAscending) {
        document.getElementById("th" + (column + 1)).innerHTML += " ▼";
    }
    
    else {
        document.getElementById("th" + (column + 1)).innerHTML += " ▲";
    }

    rows.forEach(function (row) {
        table.tBodies[0].appendChild(row);
    });
}

sortTable(0);
