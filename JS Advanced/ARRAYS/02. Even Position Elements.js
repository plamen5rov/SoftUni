function solve(input) {

    output = [];

    if (input.length == 1) {
        output = input[0];
    }

    else {

        for (let i = 0; i < input.length; i++) {
            if (i % 2 == 0) {
                output.push(input[i]);
            }


        }
        output = output.join(' ').toString();
    }

    console.log(output);
}
