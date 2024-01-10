function fetchHelloInFr () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr ',
    (helloFr) => $('div#hello').text(helloFr.hello));
}

fetchHelloInFr();
