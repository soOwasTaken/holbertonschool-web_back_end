const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(process.argv[2]);
      let response = "This is the list of our students\n";
      for (const [field, names] of Object.entries(students)) {
        response += `Number of students in ${field}: ${
          names.length
        }. List: ${names.join(", ")}\n`;
      }
      return res.status(200).send(response);
    } catch (error) {
      return res.status(500).send("Cannot load the database");
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const major = req.params.major.toUpperCase();
      if (!["CS", "SWE"].includes(major)) {
        return res.status(500).send("Major parameter must be CS or SWE");
      }
      const students = await readDatabase(process.argv[2]);
      const names = students[major] || [];
      return res.status(200).send(`List: ${names.join(", ")}`);
    } catch (error) {
      return res.status(500).send("Cannot load the database");
    }
  }
}

module.exports = StudentsController;
