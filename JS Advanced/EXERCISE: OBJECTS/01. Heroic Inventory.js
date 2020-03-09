function inventory(data){

    return JSON.stringify(data.reduce((acc, heroString, i, arr) => {

        let [name, level, items] = heroString.split(' / ')

        acc.push({name, level: Number(level), items: items ? items.split(',').map(x => x.trim()) : []})

        return acc;

        //return [...acc, {name: heroName, age, inventory}]
    }, []));
}
