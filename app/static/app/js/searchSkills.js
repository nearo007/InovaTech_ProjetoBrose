function searchSkills(input, containerId) {
    const query = input.value.trim().toLowerCase();  // Remove espaços extras
    const skillContainer = document.getElementById(containerId);
    const labels = skillContainer.querySelectorAll("label");

    labels.forEach(label => {
        const text = label.textContent.trim().toLowerCase();  // Remove espaços extras
        if (query === "") {
            label.style.display = "";  // Se a pesquisa estiver vazia, mostra tudo
        } else {
            label.style.display = text.startsWith(query) ? "" : "none";  // Aplica o filtro
        }
    });
}
