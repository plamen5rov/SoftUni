function solve(num1, num2, num3) {

    let result = 0;

    if (num1 > num2 && num1 > num3){

        result = num1;

    }
    else if (num2 > num1 && num2 > num3){

        result = num2;

    } else {result = num3}

    console.log(`The largest number is ${result}.`);
}


/// CHAOV 2

function solveDec(...params) {
    return `'The largest number is ${params.sort((a, b) => a - b).pop()}`;
}

console.log(solveDec(5, -3, 16, 18));
console.log(solveDec(-3, -5, -22.5, 0));


/// CHAOV 3

function solveMathMax(...params) {
    return `'The largest number is ${Math.max(...params)}`;
}

console.log(solveMathMax(5, -3, 16, 18));
console.log(solveMathMax(-3, -5, -22.5, 0));
