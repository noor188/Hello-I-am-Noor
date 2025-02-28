// 1. change the card transparency when user hover over a card

// 1. Setup: access elements
const cards = document.getElementsByClassName('card-body');
const card1 = document.getElementById('card1');
const card2 = document.getElementById('card2');
const card3 = document.getElementById('card3');
const card4 = document.getElementById('card4');
const card5 = document.getElementById('card5');
const card6 = document.getElementById('card6');

// 2. work: manipulation
function changTransparency1(){    
    card1.style.opacity= 0.5;   
}

function changTransparency2(){    
    card2.style.opacity= 0.5;   
}

function changTransparency3(){    
    card3.style.opacity= 0.5;   
}

function changTransparency4(){    
    card4.style.opacity= 0.5;   
}

function changTransparency5(){    
    card5.style.opacity= 0.5;   
}

function changTransparency6(){    
    card6.style.opacity= 0.5;   
}

function changTransparencyDefault1(){
    card1.style.opacity= 1;   
}

function changTransparencyDefault2(){
    card2.style.opacity= 1;   
}

function changTransparencyDefault3(){
    card3.style.opacity= 1;   
}

function changTransparencyDefault4(){
    card4.style.opacity= 1;   
}

function changTransparencyDefault5(){
    card5.style.opacity= 1;   
}

function changTransparencyDefault6(){
    card6.style.opacity= 1;   
}

// 3. event
card1.addEventListener('mouseover', changTransparency1);
card1.addEventListener('mouseout', changTransparencyDefault1);

card2.addEventListener('mouseover', changTransparency2);
card2.addEventListener('mouseout', changTransparencyDefault2);

card3.addEventListener('mouseover', changTransparency3);
card3.addEventListener('mouseout', changTransparencyDefault3);

card4.addEventListener('mouseover', changTransparency4);
card4.addEventListener('mouseout', changTransparencyDefault4);


card5.addEventListener('mouseover', changTransparency5);
card5.addEventListener('mouseout', changTransparencyDefault5);

card6.addEventListener('mouseover', changTransparency6);
card6.addEventListener('mouseout', changTransparencyDefault6);





