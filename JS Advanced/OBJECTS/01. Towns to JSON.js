function townsToJSON(input) {
    let towns = [];
    let regex = /\s*\|\s*/;

    for (let line of input.splice(1)) {
        let tokens = line.split(regex);
        
        let townObj = { Town: tokens[1], Latitude: Number(parseFloat(tokens[2]).toFixed(2)), Longitude: Number(parseFloat(tokens[3]).toFixed(2)) };
        towns.push(townObj);
    }

    //JSON.parse(towns);

    

    console.log(JSON.stringify(towns));
}
