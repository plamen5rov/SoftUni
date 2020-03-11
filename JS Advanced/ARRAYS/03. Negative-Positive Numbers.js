function solve(input) {

output = [];

for (let i = 0; i < input.length; i++) {

    if (input[i] >= 0){
        output.push(input[i]);
    } else {
        output.unshift(input[i]);
    }
    
}

    console.log(output.join('\n'));
}
