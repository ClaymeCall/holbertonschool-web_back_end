// Read the contents of a CSV file to log the count of students in each field.

// Import fs module to allow interaction with file system
const fs = require('fs');

function countStudents(path) {
	return new Promise((resolve, reject) => {
		fs.readFile(path, 'utf8', (err, data) => {
			// Handle errors
			if (err) {
				reject(new Error('Cannot load the database'));
				return;
			}
			const lines = data.split('\n').filter((line) => line.length > 0); // Split by line, and filter any empty one

			// Handle no students case
			if (lines.length <= 1) {
				resolve('Number of students: 0');
				return;
			}

			const fields = {};
			for (let i = 1; i < lines.length; i += 1) {
				const student = lines[i].split(','); // Split the data of one student by commas
				if (fields[student[3]]) {
					fields[student[3]].push(student[0]);
				} else {
					fields[student[3]] = [student[0]];
				}
			}

			// Print the list of students in each field
			let processedData = `Number of students: ${lines.length - 1}`;
			for (const field in fields) {
				if (field) {
					const list = fields[field];
					processedData += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
				}
			}

			resolve(processedData);
		});
	});
}

module.exports = countStudents;
