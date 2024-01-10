function fetchFilmTitle () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    (films) => {
      $.each(films.results, (key, val) => $('ul#list_movies').append('<li>' + val.title + '</li>'));
    });
}

fetchFilmTitle();
