function inventory(input) {

    let heroes = [];

    for (let line of input) {
        let [name, level, items] = line.split(' / ');
        level = Number(level);
        items = items ? items.split(', ') : [];
        heroes.push({ name, level, items });

    }

    return JSON.stringify(heroes);
}

//ANOTHER SOLUTION:

function inventory(data){

    return JSON.stringify(data.reduce((acc, heroString, i, arr) => {

        let [name, level, items] = heroString.split(' / ')

        acc.push({name, level: Number(level), items: items ? items.split(',').map(x => x.trim()) : []})

        return acc;

        //return [...acc, {name: heroName, age, inventory}]
    }, []));
}
