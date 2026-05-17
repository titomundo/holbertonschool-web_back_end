const express = require('express');
const fs = require('node:fs/promises');

const app = express();
const PORT = 1245;

async function countStudents(path) {
  /* honestly this code is a mess it should be divided
   * into subfunctions because wtf
   * im manually decoding a csv
  */
  try {
    const csv = await fs.readFile(path, 'utf8');
    const data = csv.split('\n');
    const rows = data.slice(1);
    const students = [];
    const degrees = [];
    const list = [];

    for (let i = 0; i < rows.length; i += 1) {
      if (rows[i] !== '') {
        const student = rows[i].split(',');
        students.push([student[0], student[3]]);
      }
    }

    degrees.push(['CS',
      students
        .filter((student) => student[1] === 'CS')
        .map((i) => i[0]),
    ]);

    degrees.push(['SWE',
      students
        .filter((student) => student[1] === 'SWE')
        .map((i) => i[0]),
    ]);

    list.push(`Number of students: ${students.length}`);
    degrees.forEach((degree) => {
      list.push(`Number of students in ${degree[0]}: ${degree[1].length}. `
        + `List: ${degree[1].join(', ')}`);
    });

    return list.join('\n');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((data) => {
      res.end(data);
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(PORT);

module.exports = app;
