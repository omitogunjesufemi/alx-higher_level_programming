function addAsyncScript () {
  const scriptVar = document.querySelector('script');
  scriptVar.setAttribute('async', '');
}

function updateHeaderColor () {
  const headerVar = document.querySelector('header');
  headerVar.style.color = '#FF0000';
}

document.addEventListener('DOMContentLoaded', () => {
  addAsyncScript();
  updateHeaderColor();
});
