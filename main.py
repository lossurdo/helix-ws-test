from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

from util import *

import logging

logger = logging.getLogger("uvicorn")
logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá! Sua API FastAPI está rodando no Render! 🎉"}


@app.get("/rest/info")
def info():
    return {
        "message": "ok"
    }


@app.post("/rest/convert-properties-to-json")
async def convert_properties_to_json(request: Request):
    obj = await request.json()
    logger.info(f"Received JSON: {obj}")

    if not obj:
        return JSONResponse(content={
            "error": "No data provided"
        })

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

    questions_and_answers_string = ""
    questions_and_answers = {}
    for qna in arrQnA:
        questions_and_answers_string += f"{qna.get('label')}@,@{qna.get('value')}@;@"
        questions_and_answers[qna.get("label")] = qna.get("value")
    map["questions_and_answers_string"] = questions_and_answers_string.rstrip("@;@")
    map["questions_and_answers"] = questions_and_answers

    return JSONResponse(content=map)


@app.post("/rest/get-value-from-json")
async def get_value_from_json(
    request: Request,
    key: str = Query(..., description="Key to search for"),
    qna: bool = Query(False, description="Search in questions_and_answers")
):

    obj = await request.json()
    logger.info(f"Received JSON: {obj}")

    if qna:
        qna_obj = obj.get("questions_and_answers")
        if not qna_obj or key not in qna_obj:
            return PlainTextResponse(status_code=404)
        return PlainTextResponse(content=qna_obj.get(key))

    if key not in obj:
        return PlainTextResponse(status_code=404)

    return PlainTextResponse(content=obj.get(key))


@app.post("/rest/prepare-for-auto")
async def prepare_for_auto(
    request: Request,
    auto_ident: str = Query(..., description="Identifier for the automation"),
    auto_action: str = Query(..., description="Action to perform")
):

    obj = await request.json()
    logger.info(f"Received JSON: {obj}")

    payload = {
        "helixTaskId": obj.get("id"),
        "autoIdent": auto_ident,
        "autoAction": auto_action,
        "fallbackHelixGroup": "DES-AUTO",
        "params": []
    }

    for key, value in obj.get("questions_and_answers", {}).items():
        payload["params"].append({
            "key": key,
            "value": value
        })

    payload["params"].append({
        "key": "submitted_date",
        "value": obj.get("submitted_date")
    })
    payload["params"].append({
        "key": "service_name",
        "value": obj.get("service_name")
    })
    payload["params"].append({
        "key": "requestedby_full_name",
        "value": obj.get("requestedby_full_name")
    })
    payload["params"].append({
        "key": "requestedby_login_name",
        "value": obj.get("requestedby_login_name")
    })
    payload["params"].append({
        "key": "requestedby_company",
        "value": obj.get("requestedby_company")
    })
    payload["params"].append({
        "key": "requestedby_organization",
        "value": obj.get("requestedby_organization")
    })
    payload["params"].append({
        "key": "requestedby_department",
        "value": obj.get("requestedby_department")
    })
    payload["params"].append({
        "key": "requestedby_job_title",
        "value": obj.get("requestedby_job_title")
    })
    payload["params"].append({
        "key": "requestedfor_full_name",
        "value": obj.get("requestedfor_full_name")
    })
    payload["params"].append({
        "key": "requestedfor_login_name",
        "value": obj.get("requestedfor_login_name")
    })
    payload["params"].append({
        "key": "requestedfor_company",
        "value": obj.get("requestedfor_company")
    })
    payload["params"].append({
        "key": "requestedfor_organization",
        "value": obj.get("requestedfor_organization")
    })
    payload["params"].append({
        "key": "requestedfor_department",
        "value": obj.get("requestedfor_department")
    })
    payload["params"].append({
        "key": "requestedfor_job_title",
        "value": obj.get("requestedfor_job_title")
    })
    payload["params"].append({
        "key": "submitter_full_name",
        "value": obj.get("submitter_full_name")
    })
    payload["params"].append({
        "key": "submitter_login_name",
        "value": obj.get("submitter_login_name")
    })
    payload["params"].append({
        "key": "submitter_company",
        "value": obj.get("submitter_company")
    })
    payload["params"].append({
        "key": "submitter_organization",
        "value": obj.get("submitter_organization")
    })
    payload["params"].append({
        "key": "submitter_department",
        "value": obj.get("submitter_department")
    })
    payload["params"].append({
        "key": "submitter_job_title",
        "value": obj.get("submitter_job_title")
    })

    for param in payload["params"]:
        param["key"] = format_key_for_auto(param["key"])

    return JSONResponse(content=payload)