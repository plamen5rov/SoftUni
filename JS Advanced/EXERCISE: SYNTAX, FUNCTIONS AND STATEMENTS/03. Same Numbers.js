function solve(num) {

    let number = num.toString();
    let length = number.length;



    let sum = 0;

    let equal = true;

    for (let index = 0; index < length; index++) {
        const element = +number[index];

        sum += element;

        if (index < length - 1){

        if (element == Number(number[index + 1])) {

            equal = true;

        } else {

            equal = false;
        }
    }

    }

    console.log(equal);

    console.log(sum);

}
