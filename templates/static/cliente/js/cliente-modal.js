// Aqui o modal será aberto ou fechado
const openModalButton = document.querySelector("#open-modal");
const closeModalButton = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

const toggleModal = () => {
  modal.classList.toggle("hide");
  fade.classList.toggle("hide");
};

[openModalButton, closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});

// Responsável por fazer o next step do modal
const modalSteps = document.querySelectorAll('.modal-all')
const prevBtns = document.querySelectorAll('.button-prev');
const nextBtns = document.querySelectorAll('.button-next');

let modalStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    modalStepsNum++;
    updateModalSteps();
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    modalStepsNum--;
    updateModalSteps();
  });
});

function updateModalSteps() {
  modalSteps.forEach(modalStep => {
    modalStep.classList.contains('modal-step-active') && modalStep.classList.remove('modal-step-active')
  })

  modalSteps[modalStepsNum].classList.add("modal-step-active")

}

// Analisa valor a cada atualização do input e verifica se possui saldo
// TODO verificar se é um double
var valorPix = document.querySelector('#valor-pix')

valorPix.addEventListener('input', () => {
  verificaValor(valorPix.value)
})

function verificaValor(valor) {
  const data = {
    saldo: parseFloat(valor)
  }
  fetch('http://127.0.0.1:8000/api/clientes/verificar_saldo', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json" // Especifica o tipo de conteúdo como JSON
    },
    body: JSON.stringify(data)
  }).then(response => response.json())
  .then(result => console.log(result))
  .catch(err => console.log('Erro na requisição:', err))
}

// Botão de pagamento
const botaoReqDados = document.querySelector("#req-dados");

// Adiciona um evento de clique ao botão
botaoReqDados.addEventListener("click", () => {
    getDadosComPix();
});


function getDadosComPix() {

  const data = {
    chave_pix: document.querySelector('#chave-pix').value
  }

  fetch('http://127.0.0.1:8000/api/transacoes/pagamentos/pix', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json" // Especifica o tipo de conteúdo como JSON
    },
    body: JSON.stringify(data)
  }).then(response => response.json())
    .then(result => {

      modalSteps.forEach(modalStep => {
        modalStep.classList.contains('modal-step-active') && modalStep.classList.remove('modal-step-active')
      })

      document.querySelector('.modal-pagamento').classList.add('modal-step-active')

      document.querySelector('#dados-recebedor').innerHTML = `<span>Beneficiário: ${result['nome']}</span><br><span>CPF: ${result['cpf']}</span><br><span>Banco: ${result['banco']}</span>`

      console.log(result)
    })
    .catch(err=> console.log(err))
}

function realizarPagamento() {

}