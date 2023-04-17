'use strict' // uses modern javascript functionality

let a, // can use within block of code (these are also undefined)
b,
c;

var d; // can use within all of function

const e = 2; // does not change
let n = null // null value

typeof(e); // get type of variable

r = prompt("What's Up?", "Not much") //input prompt with default value supplied
String(e) // convert to string
Number(e) //to number, default to NaN when not possible
Boolean(1) // true

r = +'e' // converts to number
1 + 2 + r + 3 // evaluates from right to left

'a' > 'b' // returns false: a is first in alphabet

let v = (r==4) ? 4 : 10; // sets v to 4 or 10 depending on r

let age = '10';
let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';

if (age == 10 || age == 20){
    var v = 'multiple of 10'
}

a ?? b // if a is undefined, then b

alert (a ?? b ?? 'Unknown') // shows first defined value

let i = 0;
while (i > 10){
    i++
} // can switch around with do {} while to check condition after functuon call


let b = 0
for (let i=0; i++; i==1){
    b++
    if (b == 2){
        break; // breaks entire loop
        continue; //skips to next loop
    }
}

switch (x){
    case x == 2:
        b = true;
        break;

    case x == 3:
        b = false;
        break;
}

let obj = {
    name: "Will",
    age: 20,
    [b]: 10,
    ["Fruit Time"]: false,
};

obj.age = 21;
obj["Fruit Time"] = true;

let key = "name"
if (key in obj){
    alert(true);
}

let objCopy = obj; // changes to obj2 also changes obj - they point to same object
let obj3 = {};
Object.assign(obj3, obj.name)

class User{
    constructor(name){
        this.name = name;
    }

    sayHi(){
        alert(this.name);
    }

    get name(){
        return this.name;
    }

}

class SpecialUser extends User{
    constructor(age){
        super(name);
        this.age = age;
    }
    age(){
        return ('${this.name} is old!')
    }
}






