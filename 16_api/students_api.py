from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0)


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=0)


class Student(StudentCreate):
    id: int


app = FastAPI(title="Students API")

students = {
    1: Student(id=1, name="Alice", age=20),
    2: Student(id=2, name="Bob", age=22),
    3: Student(id=3, name="Charlie", age=21),
}


def get_or_404(student_id):
    student = students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/students")
def list_students():
    return list(students.values())


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return get_or_404(student_id)


@app.post("/students", status_code=201)
def create_student(data: StudentCreate):
    new_id = max(students, default=0) + 1
    student = Student(id=new_id, **data.model_dump())
    students[new_id] = student
    return student


@app.patch("/students/{student_id}")
def update_student(student_id: int, data: StudentUpdate):
    student = get_or_404(student_id)
    updated = student.model_copy(update=data.model_dump(exclude_unset=True))
    students[student_id] = updated
    return updated


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    get_or_404(student_id)
    del students[student_id]
    return Response(status_code=204)
