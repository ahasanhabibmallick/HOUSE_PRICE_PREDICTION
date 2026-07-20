from fastapi import FastAPI,HTTPException
from pydantic import BaseModel 

app = FastAPI()

students = {
    "S001": {"name": "Ravi", "marks":86, "grade":"A"},
    "S002": {"name": "Kishan", "marks":87, "grade":"B"},
    "S003": {"name": "Modi", "marks":88, "grade":"D"},
    "S004": {"name": "Mamata", "marks":89, "grade":"C"},
}


class MarkSubmission(BaseModel):
    student_id: str
    marks:int
    subject: str

@app.get("/student/{student_id}")
def get_student(student_id:str):
    if student_id not in students:
        raise HTTPException(
           status_code=404,
           detail = f"student with ID {student_id} does not exist"
        )
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission:MarkSubmission):
    #error 1 students does not exist
    if submission.student_id not in students:
       raise HTTPException(
           status_code=404,
           detail = f"student with ID {submission.student_id} does not exist"
        ) 
    #error 2 validrange 0-100
    if submission.marks < 0 or submission.marks >100:
        raise HTTPException(
            status_code=400,
            detail ={
                "error":"marks must be between 0 and 100 ",
                "marks_received":submission.marks,
                "fix":"enter a valid value between 0 and 100"   
            }
        )
    # error 3 subject name empty
    if submission.subject.strip() == "":
        raise HTTPException(
            status_code=400,
            detail = "subject name can not be empty"
        )
    try:
        students[submission.student_id]['marks'] = submission.marks
        return {
        "message":"marks submitted successfully",
        "student":students[submission.student_id]["name"],
        "subject":submission.subject,
        "marks":submission.marks
    }

    except Exception as e:
        raise HTTPException(
         status_code=500,
         detail=f"Something went wrong from our side:{str(e)}"
        )