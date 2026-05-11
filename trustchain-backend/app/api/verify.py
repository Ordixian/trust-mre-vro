from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.core.scoring import calculate_trust_score
import random # Placeholder for real AI logic

router = APIRouter()

@router.post("/run")
async def verify_submission(
    product_name: str = Form(...),
    nafdac_no: str = Form(...),
    price: float = Form(...),
    vendor_name: str = Form(...),
    image: UploadFile = File(...)
):
    try:
        # Placeholder for OCR/AI logic (Phase 2)
        # In real-life, this is where EasyOCR/Google Vision runs
        
        mock_product_data = {
            "is_nafdac_valid": nafdac_no.startswith("A7"), 
            "price": price,
            "market_avg": 5000,
            "expiry_status": "active"
        }
        
        mock_vendor_data = {
            "years_in_business": 2,
            "complaint_count": 0,
            "is_cac_registered": True
        }

        analysis = calculate_trust_score(mock_product_data, mock_vendor_data)

        return {
            "id": f"TRC-{random.randint(1000, 9999)}",
            "product": product_name,
            "vendor": vendor_name,
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))