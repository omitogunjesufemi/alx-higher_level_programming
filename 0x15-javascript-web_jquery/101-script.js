function crudListOnClick () {
  $('div#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').on('click', () => {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
}

$(document).ready(() => {
    crudListOnClick()
});
