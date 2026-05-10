export default function (arr) {
  if (!Array.isArray(arr)) {
    return [];
  }

  return arr.map((i) => i.id);
}
