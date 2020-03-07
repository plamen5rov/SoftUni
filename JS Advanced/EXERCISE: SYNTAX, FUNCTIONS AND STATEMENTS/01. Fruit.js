function fruit(fruit, weight, price){

let name = fruit;
let kg = weight / 1000;
let cena = price;
let money = kg * cena;

console.log(`I need $${money.toFixed(2)} to buy ${kg.toFixed(2)} kilograms ${name}.`)


}
