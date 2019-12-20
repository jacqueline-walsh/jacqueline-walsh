// ES6 Class
class TypeWriter {

    constructor(txtElement, words, wait=3000) {
      this.txtElement = txtElement;
      this.words = words;
      this.txt = '';
      this.wordIndex = 0;
      this.wait = parseInt(wait, 10);
      this.type();
      this.isDeleting = false;
    }

    type() {
  // current index of word
  const current = this.wordIndex % this.words.length;
  // Get full text of current word
  const fulltext = this.words[current];
  // check if deleting
  if (this.isDeleting) {
    // remove char
    this.txt = fulltext.substring(0, this.txt.length - 1);
  } else {
    // add char
    this.txt = fulltext.substring(0, this.txt.length + 1);
  }
  // insert txt into element
  this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

  // Initial type speed
  let typeSpeed = 300;

  if (this.isDeleting) {
    typeSpeed /- 2;
  }

  // if word is complete
  if (!this.isDeleting && this.txt === fulltext) {
    // this will give a pause at the end of the word
    typeSpeed = this.wait;
    // set is deleting to true
    this.isDeleting = true;
  } else if(this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    // Move to next word
    this.wordIndex++;
    // Pause before retyping next word
    typeSpeed = 500;
  }

  setTimeout(() => this.type(), typeSpeed);      
    }
}

// Init on DOM Load
document.addEventListener('DOMContentLoaded', init);

function init() {
  const txtElement = document.querySelector('.txt-type');
  const words = JSON.parse(txtElement.getAttribute('data-words'));
  const wait = txtElement.getAttribute('data-wait');  
  // Init typewriter
  new TypeWriter(txtElement, words, wait);
}

