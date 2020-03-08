function solve(input){

    input = input.toString();
    let text = input
    .match(/\w+/gim)
    .reduce((a, b) => {
        if (typeof a[b] === 'undefined'){
            a[b] = 0;
        }
        a[b]++;
        return a;
    }, {});

    let output = JSON.stringify(text);

    console.log(output);

}
