var restart = document.querySelector("#restart");

var squares = document.querySelectorAll('td');

function clearBoard(){
    for(var i =0 ;i < squares.length;i++ ){
        squares[i].textContent='';
    }
}

function changeMarker(){
    if (this.textContent === ''){
        this.textContent="X"
    }else if (this.textContent === "X"){
        this.textContent ="O"
    }else{
        this.textContent=""
    }
}

for (var i = 0; i < squares.length;i++){
    squares[i].addEventListener('click',changeMarker)
}



restart.addEventListener('click',clearBoard);