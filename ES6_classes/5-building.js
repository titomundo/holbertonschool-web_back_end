export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    if (!(this.prototype instanceof Building) && !Object.hasOwn(this, 'evacuationWarningMessage')) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  evacuationWarningMessage() { }
}
