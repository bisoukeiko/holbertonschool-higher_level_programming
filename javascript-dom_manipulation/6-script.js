fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('fetch failed');
    }
    return response.json();
  })
  .then((data) => {
    const element = document.querySelector('#character');
    element.innerHTML = data.name;
  })
  .catch((error) => console.error('error:', error));
