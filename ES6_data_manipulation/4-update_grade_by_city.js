export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: (newGrades.find((grade) => grade.studentId === student.id) || { grade: 'N/A' }).grade,
    }));
}
