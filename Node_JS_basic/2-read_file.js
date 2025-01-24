// Read the contents of a CSV file to log the count of students in each field.

// Import fs module to allow interaction with file system
const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf8'); // Store the files data in a variable
    const lines = data.split('\n').filter((line) => line);// Split by line, and filter any empty one
    const fields = {};
    lines.forEach((line) => {
      const student = line.split(','); // Split the data by commas

      // If the current field is not in the list, add it
      if (!fields[student[3]]) fields[student[3]] = [];
      fields[student[3]].push(student[0]);
    });

    // Log the count of students
    console.log(`Number of students: ${lines.length - 1}`);

    // Print the list of students in each field
    for (const field in fields) {
      if (field) {
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
