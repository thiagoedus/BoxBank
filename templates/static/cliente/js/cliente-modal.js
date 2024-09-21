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