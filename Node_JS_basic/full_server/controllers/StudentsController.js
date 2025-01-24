import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const db = process.argv[2];
    readDatabase(db)
      .then((students) => {
        let response = 'This is the list of our students';
        Object.keys(students).sort().forEach((field) => {
          response += `\nNumber of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`;
        });
        res.status(200).send(response);
      })
      .catch((error) => {
        res.status(500).send(error.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    const db = process.argv[2];
    return readDatabase(db)
      .then((students) => {
        if (!students[major]) {
          return res.status(500).send('Major parameter must be CS or SWE');
        }
        return res.status(200).send(`List: ${students[major].join(', ')}`);
      })
      .catch((error) => {
        res.status(500).send(error.message);
      });
  }
}

export default StudentsController;
