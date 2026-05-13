@router.post("/run")
async def verify_submission(...):
    # Skip the heavy OCR scanning to save memory
    # Just check if the NAFDAC number starts with 'A7' (example logic)
    is_nafdac_valid = nafdac_no.startswith("A7")

    mock_product_data = {
        "is_nafdac_valid": is_nafdac_valid, 
        "price": price,
        "market_avg": 5000,
        "expiry_status": "active"
    }
    
    analysis = calculate_trust_score(mock_product_data, mock_vendor_data)
    return {"id": "TRC-DEMO", "analysis": analysis}
