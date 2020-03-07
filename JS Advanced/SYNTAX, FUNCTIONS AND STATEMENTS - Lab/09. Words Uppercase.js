function solve(text) {
   output = text.match(/\w+/gim)
        .map(x => x.toUpperCase());
  
  console.log(output.join(", "));
}

