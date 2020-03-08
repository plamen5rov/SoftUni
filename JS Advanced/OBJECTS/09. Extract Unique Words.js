function solve(input){

    let output = [...new Set(input
        .join("")
        .toLowerCase()
        .match(/\w+/gim)
        )].join(", ")


    console.log(output);

}
