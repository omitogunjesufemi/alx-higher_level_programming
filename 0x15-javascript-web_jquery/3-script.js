function updateHeaderClassOnClick () {
  $('div#red_header').on('click', () => {
    $('header').addClass('red');
  });
}

updateHeaderClassOnClick();
