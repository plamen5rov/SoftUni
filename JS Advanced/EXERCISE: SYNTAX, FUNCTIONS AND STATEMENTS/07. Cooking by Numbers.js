function solve(input) {

    let number = Number(input.shift());



    //console.log(input);

    for (let i = 0; i < input.length; i++) {

        let command = input[i];

        switch (command) {
            case 'chop':

                number = number / 2;

                console.log(number);

                break;

            case 'dice':

                number = Math.sqrt(number);

                console.log(number);

                break;

            case 'spice':

                number += 1;

                console.log(number);

                break;

            case 'bake':

                number = number * 3;

                console.log(number);

                break;

            case 'fillet':

                number = number * 0.8;

                console.log(number.toFixed(1));

                break;

            default:
                break;
        }
    }

}

