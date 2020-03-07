function solve(input = 5) {

    for (let index = 1; index <= input; index++) {
        console.log('* '.repeat(input));
        
    }
    
}

// Chaov

function solve(size = 5) {
    let result = new Array(size);

    for (let i = 0; i < size; i++) {
        result[i] = "* ".repeat(size).trim();
    }

    return result.join("\n");
}

console.log(solve());
console.log(solve(2));
console.log(solve(4));
