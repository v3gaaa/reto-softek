"""
from fastapi import APIRouter, HTTPException
from app.models.get_request_data import get_request_data_review_info

router = APIRouter()

@router.get("/get-review-info/{request_id}/")
async def get_review_info(request_id: str):
    try:
        request_data = get_request_data_review_info(request_id)  # Función que obtenga datos de Firestore
        if not request_data:
            raise HTTPException(status_code=404, detail="Request not found")
        
        documents = request_data.get("documents", {})
        
        document_status = {}
        for doc_name, doc_content in documents.items():
            document_status[doc_name] = {
                "content": doc_content,
                "legible": True  # Aquí puedes implementar tu lógica para determinar si es legible
            }
        
        return {
            "name": request_data["name"],
            "email": request_data["email"],
            "income": request_data["annual_income"],
            "credit_score": request_data["risk_score"],
            "phone": request_data["phone"],
            "documents": document_status
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
from fastapi import APIRouter, HTTPException
from app.models.get_request_data import get_request_data_all

router = APIRouter()

@router.get("/get-review-info/{request_id}/")
async def get_review_info(request_id: str):
    """
    Returns a more information of a request.
    "name": "Spiegelin",
    "email": "test@test.com",
    "income": 10000000.0,
    "credit_score": 0.0,
    "risk_score": 0.0,
    "phone": "3333333333",
    "status": "Under Review",
    "documents": {
        "Elements of Python Programming.pdf": {
            "legible": true
        },
        "Búsqueda y Ordenamiento.pdf": {
            "legible": true
        },
        "Abraham Silberschatz-Operating System Concepts (9th,2012_12).pdf": {
            "legible": true
        }
    }
    """
    try:
        request_data = get_request_data_all(request_id)  # Función que obtenga datos de Firestore
        if not request_data:
            raise HTTPException(status_code=404, detail="Request not found")
        
        documents = request_data.get("documents", {})
        
        document_status = {}
        for doc_name, doc_content in documents.items():
            #document_status[doc_name] = {
            document_status[doc_name] = {
                #"content": doc_content["filename"], #doc_content da todo
                "legible": True  # Lógica para determinar si es legible
            }
        
        return {
            "name": request_data["name"],
            "email": request_data["email"],
            "income": request_data["annual_income"],
            "credit_score": request_data["risk_score"],
            "phone": request_data["phone"],
            "status": request_data["status"],
            "documents": document_status,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



