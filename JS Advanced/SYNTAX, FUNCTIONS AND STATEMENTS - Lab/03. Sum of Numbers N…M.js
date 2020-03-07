function solve(n, m) {

    let first = Number(n);
    let second = Number(m);
    let sum = 0

    for (let index = first; index <= second; index++) {
        sum += index;

    }

    console.log(sum);
}


//CHAOV VERSION:

function solve(n, m) {
    let result = 0;
    for (let i = Number(n); i <= Number(m); i++) {
        result += i;
    }
    return result;
}
