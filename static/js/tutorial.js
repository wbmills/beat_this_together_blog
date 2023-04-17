let value = 12;
let name = 'bob';

// comment

/* long
comment
 */

function m(x, y){
    return x * y
}

let v = m(2,3)

function createParagraph() {
  const para = document.createElement("p");
  para.textContent = "You clicked the button!";
  document.body.appendChild(para);
}

var id = null;
function myMove() {
  var elem = document.getElementById("myAnimation");
  var pos = 0;
  clearInterval(id);
  id = setInterval(frame, 10);
  var end = false;
  function frame() {
    if (pos == 350) {
       while (pos != 0){
            pos--;
            elem.style.top = pos - 'px';
            elem.style.right = pos - 'px';
       }
    } else {
        pos++;
        elem.style.top = pos + 'px';
        elem.style.left = pos + 'px';
    }
  }
}

function checkNumber(){
    var x = document.getElementById('guess').value;
    var y = Math.floor(Math.random() * 2)
    alert(x)
    alert(y)
    if (x == y){
        alert("Correct!");}
    else{
        alert("Wrong");
    }
}
