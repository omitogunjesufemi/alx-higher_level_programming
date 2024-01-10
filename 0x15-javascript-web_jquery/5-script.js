function addListOnClick () {
  $('div#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
}

addListOnClick();
