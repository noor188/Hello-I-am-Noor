// 2. Automatically change my name color every second

// 1. setup
const colors = ['red', 'blue', 'green', 'orange', 'purple'];
let colorIndex = 0;
const namePart = document.getElementById('name-id');

// 2. work: manipulation
function changeColorName(){
    namePart.style.color = colors[colorIndex];
    colorIndex = (colorIndex +1) % colors.length;
}

// 3. event
setInterval(changeColorName, 1000);


// change table caption color 

// 1. setup
const caption = document.getElementById('media-id');

// 2. work: manipulation
function changeColor(){
    console.log('inside');
    if(caption.style.color ="black"){
        caption.style.color = "red";
    }    
}

// 3. event
caption.addEventListener('mouseover', changeColor);
