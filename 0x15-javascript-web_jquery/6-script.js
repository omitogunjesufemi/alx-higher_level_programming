function updateHeaderTextOnClick () {
  $('div#update_header').on('click', () => {
    $('header').text('New Header!!!');
  });
}

updateHeaderTextOnClick();
