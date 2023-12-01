const fs = require('fs').promises;

const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.split('\n').filter((line) => line);
    const students = {};

    lines.slice(1).forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstName);
    });

    return students;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = { readDatabase };
