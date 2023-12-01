const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.promises
      .readFile(path, 'utf8')
      .then((data) => {
        const lines = data.split('\n');
        const filteredLines = lines.filter((line) => line.trim());

        if (filteredLines.length < 2) {
          throw new Error('No students found');
        }

        const students = filteredLines.slice(1);
        const count = students.length;
        console.log(`Number of students: ${count}`);

        const fields = {};
        students.forEach((student) => {
          const [, , , field] = student.split(',');
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(student.split(',')[0]);
        });

        for (const [field, names] of Object.entries(fields)) {
          console.log(
            `Number of students in ${field}: ${
              names.length
            }. List: ${names.join(', ')}`,
          );
        }

        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
