function solve(input) {
    let checkLength = input.length;

    let first = Number(input.shift());

    let last = Number(input.pop());



    if (checkLength == 1) {
        result = first * 2;
    } else {
        result = first + last;
    }

    console.log(result);
}
