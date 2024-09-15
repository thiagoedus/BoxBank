const codigo_boleto = document.querySelector("#valor-boleto");
const openModalButton = document.querySelector("#open-modal");
const closeModalButton = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

// TODO Tratar valor diferente de 0
const exibe_dados = (dados) => {
  var valorBoleto = document.querySelector('#valor-boleto-digitado');
  valorBoleto.innerHTML = codigo_boleto.value;
}

function toggleModal() {
  exibe_dados();
  modal.classList.toggle("hide");
  fade.classList.toggle("hide");
}

[openModalButton, closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});
