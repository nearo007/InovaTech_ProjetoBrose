document.getElementById('abc').addEventListener('input', function() {
    let pin = this.value;
    let cadastroBtn = document.querySelector('.signupBtn');
    
    if (pin === '12345') {
        cadastroBtn.style.backgroundColor = 'rgb(236, 43, 75)';
        cadastroBtn.style.color = 'white';
    }
    
    else {
        cadastroBtn.style.backgroundColor = 'rgb(122, 122, 122)';
        cadastroBtn.style.color = 'rgb(238, 238, 238)';
    }
});