export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const arr = new DataView(buff);

  if (position > length || position < 0) {
    throw RangeError('Position outside range');
  }

  arr.setInt8(position, value);
  return arr;
}
