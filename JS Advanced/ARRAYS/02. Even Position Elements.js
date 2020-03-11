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

//ALTERNATIVE SOLUTION (CHAOV)

function solve(arr){
 return arr
    .filter((_, i) => i % 2 === 0)
    .join(" "):
}
