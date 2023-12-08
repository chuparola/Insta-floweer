// Função para exibir a mensagem quando o link for clicado
document.getElementById("meuLink").addEventListener("click", function() {
    // Exibe a mensagem
    document.getElementById("mensagem").style.display = "block";

    // Define um tempo para ocultar a mensagem após alguns segundos (opcional)
    setTimeout(function() {
        document.getElementById("mensagem").style.display = "none";
    }, 3000); // Tempo em milissegundos (3 segundos neste exemplo)
});