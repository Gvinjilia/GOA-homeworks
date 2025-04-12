let selectedRating = "";
if (window.location.href.includes("index.html")) {
  const buttons = document.querySelectorAll('.btn1');
  const submitBtn = document.querySelector('.submit');

  buttons.forEach(button => button.addEventListener('click', () => {
    selectedRating = button.textContent;
    button.classList.add('selected');
  }));

  submitBtn.addEventListener('click', () => {
    if (selectedRating) {
      window.location.href = `index1.html?rating=${selectedRating}`;
    }
  });
}

if (window.location.href.includes("index1.html")) {
  const rating = window.location.href.split('rating=')[1];
  const div = document.querySelector('.selection-div');
  if (rating) {
    div.textContent = `You selected ${rating} out of 5`;
    div.style.color = 'hsl(25, 97%, 53%)';
    div.style.fontFamily = '"Overpass", sans-serif';
    div.style.fontSize = '14px';
    div.style.textAlign = 'center';
    div.style.paddingTop = '5px'
  }
};