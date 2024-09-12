const codigo_boleto = document.querySelector("#codigo-boleto");
const openModalButton = document.querySelector("#open-modal");
const closeModalButton = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

const exibe_dados = (dados) => {
  var favorecido = document.querySelector('#span-favorecido');
  var banco = document.querySelector('#span-banco');
  var valor = document.querySelector('#span-valor');
  favorecido.innerHTML = dados['favorecido'];
  banco.innerHTML = dados['emissor'];
  valor.innerHTML = dados['valor'];
}

//TODO Escolher qual modal virá para esta função
function toggleModal() {
  fetch("http://127.0.0.1:8000/api/operacoes/" + codigo_boleto.value, {
    method: "GET",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erro na requisição: " + response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      modal.classList.toggle("hide");
      fade.classList.toggle("hide");
    
      console.log(data)
      exibe_dados(data);
    })
    .catch(error => {
      // Verifica se o erro é devido a um 404
      if (error.message.includes('404')) {
        alert('Erro 404: Recurso não encontrado.'); // Exibe uma mensagem para o usuário
      } else {
        alert('Ocorreu um erro ao buscar os dados: ' + error.message); // Exibe outra mensagem genérica
      }
      console.error('Erro capturado:', error); // Também exibe o erro no console (para depuração)
    });

    // console.log(error)

};

[openModalButton, closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});
