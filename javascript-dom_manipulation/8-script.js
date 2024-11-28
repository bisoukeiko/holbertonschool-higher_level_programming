fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => {
    if (!response.ok) {
      throw new Error('fetch failed');
    }
    return response.json();
  })
  .then((data) => {
    const element = document.querySelector('#hello');
    element.textContent = data.hello;
  })
  .catch((error) => console.error('error:', error));
