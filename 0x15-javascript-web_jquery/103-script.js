function fetchHelloInLang () {
  const lang = $('input#language_code').val();
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
    (greeting) => {
      $('div#hello').text(greeting.hello);
    });
}

$(document).ready(() => {
  $('input#btn_translate').on('click', () => fetchHelloInLang());

  $('input#language_code').on('keypress', (event) => {
    if (event.which === 13) {
	fetchHelloInLang();
    }
  });
});
