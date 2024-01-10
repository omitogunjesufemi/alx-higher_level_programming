function updateHeaderColorOnClick () {
  $('div#red_header').on('click', () => {
    $('header').css('color', '#FF0000');
  });
}

updateHeaderColorOnClick();
