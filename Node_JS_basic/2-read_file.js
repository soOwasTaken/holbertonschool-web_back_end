const fs = require("fs");

function countStudents(path) {
  let content;

  try {
    content = fs.readFileSync(path, { encoding: "utf8" });
  } catch (error) {
    throw new Error("Cannot load the database");
  }

  const lines = content.split("\n").filter((line) => line.trim());
  const students = lines.slice(1); // Skip the header row

  console.log(`Number of students: ${students.length}`);

  const fieldCounts = {};
  students.forEach((student) => {
    const [, , field] = student.split(",");
    if (!fieldCounts[field]) {
      fieldCounts[field] = [];
    }
    fieldCounts[field].push(student.split(",")[0]);
  });

  Object.keys(fieldCounts).forEach((field) => {
    console.log(
      `Number of students in ${field}: ${
        fieldCounts[field].length
      }. List: ${fieldCounts[field].join(", ")}`
    );
  });
}

module.exports = countStudents;
