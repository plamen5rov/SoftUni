class Person {
  constructor(first, last) {
    this._first = first;
    this._last = last;
  }
 
  get firstName() {
    return this._first;
  }
 
  set firstName(name) {
    return (this._first = name);
  }
 
  get lastName() {
    return this._last;
  }
 
  set lastName(name) {
    return (this._last = name);
  }
 
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
 
  set fullName(name) {
    let names = name.split(" ");
    if (names.length === 2) {
      this.firstName = names[0];
      this.lastName = names[1];
    }
    return `${this.firstName} ${this.lastName}`;
  }
}
