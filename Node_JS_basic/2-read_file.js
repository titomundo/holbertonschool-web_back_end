const fs = require('node:fs');

function countStudents(path) {
  try {
    const csv = fs.readFileSync(path, 'utf8');
    const data = csv.split('\n');
    const rows = data.slice(1);
    const students = [];
    const degrees = [];

    for (let i = 0; i < rows.length; i += 1) {
      if (rows[i] !== '') {
        const student = rows[i].split(',');
        students.push([student[0], student[3]]);
      }
    }

    console.log(`Number of students: ${students.length}`);

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

    degrees.forEach((degree) => {
      console.log(`Number of students in ${degree[0]}: ${degree[1].length}. `
        + `List: ${degree[1].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
