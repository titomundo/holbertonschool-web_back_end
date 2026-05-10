export default function updateStudentGradeByCity(arr, city, newGrades) {
  const students = arr.filter((student) => student.location === city);
  const graded = students.map((student) => {
    const grade = newGrades.find((g) => g.studentId === student.id);
    if (!grade) {
      return { ...student, grade: 'N/A' };
    }

    return { ...student, grade: grade.grade };
  });

  return graded;
}
