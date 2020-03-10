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
