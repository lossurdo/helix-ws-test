from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá! Sua API FastAPI está rodando no Render! 🎉"}


@app.get("/rest/info")
def info():
    return {
        "message": "ok"
    }


@app.post("/convert-properties-to-json")
async def convert_properties_to_json(request: Request):
    arr = await request.json()
    obj = arr[0]

    objServiceRequest = obj.get("serviceRequest", {})
    objService = obj.get("service", {})
    objRequestedBy = obj.get("requestedBy", {})
    objRequestedFor = obj.get("requestedFor", {})
    objSubmitter = obj.get("submitter", {})
    arrQnA = obj.get("questionsAndAnswers", [])

    map = {
        "id": objServiceRequest.get("id"),
        "submitted_date": objServiceRequest.get("submittedDate"),
        "service_name": objService.get("name"),
        "requestedby_full_name": objRequestedBy.get("fullName"),
        "requestedby_login_name": objRequestedBy.get("loginName"),
        "requestedby_company": objRequestedBy.get("company"),
        "requestedby_organization": objRequestedBy.get("organization"),
        "requestedby_department": objRequestedBy.get("department"),
        "requestedby_job_title": objRequestedBy.get("jobTitle"),
        "requestedfor_full_name": objRequestedFor.get("fullName"),
        "requestedfor_login_name": objRequestedFor.get("loginName"),
        "requestedfor_company": objRequestedFor.get("company"),
        "requestedfor_organization": objRequestedFor.get("organization"),
        "requestedfor_department": objRequestedFor.get("department"),
        "requestedfor_job_title": objRequestedFor.get("jobTitle"),
        "submitter_full_name": objSubmitter.get("fullName"),
        "submitter_login_name": objSubmitter.get("loginName"),
        "submitter_company": objSubmitter.get("company"),
        "submitter_organization": objSubmitter.get("organization"),
        "submitter_department": objSubmitter.get("department"),
        "submitter_job_title": objSubmitter.get("jobTitle"),
    }

    questions_and_answers = {}
    for qna in arrQnA:
        questions_and_answers[qna.get("label")] = qna.get("value")
    map["questions_and_answers"] = questions_and_answers

    return JSONResponse(content=map)
