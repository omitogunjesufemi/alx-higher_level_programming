function fetchCharacterName () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    (person) => $('div#character').text(person.name));
}

fetchCharacterName();
