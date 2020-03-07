function solve(input) {

    type = typeof(input);

    if (type === 'number' ){
        radius = input;
        result = Math.pow(input,2) * Math.PI;
        console.log(result.toFixed(2));
    } else{
        console.log(`We can not calculate the circle area, because we receive a ${type}.`); 
    }
    
}
