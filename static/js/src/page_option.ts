const optionButton = document.getElementsByClassName('option_button');
const appendOption = document.querySelectorAll<HTMLDivElement>('#append_option');

optionButton[0].addEventListener('click', () => {
    let test = document.createElement('div');
    let select = document.querySelectorAll<HTMLSelectElement>('.option_item').item(0);
    test.setAttribute('class', 'option');
    test.textContent = select.value;
    appendOption.item(0).appendChild(test);

});


