export default function cleanSet(set, startString) {
  let str = '';

  if (startString === '' || (typeof startString !== 'string')) {
    return '';
  }

  const arr = Array.from(set);
  for (let i = 0; i < arr.length; i += 1) {
    if (arr[i].startsWith(startString)) {
      if (i + 1 <= arr.length && i > 0) {
        str += '-';
      }

      str += arr[i].replace(startString, '');
    }
  }

  return str;
}
