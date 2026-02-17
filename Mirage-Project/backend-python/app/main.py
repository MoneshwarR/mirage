from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from . import engine_ela, engine_ai
import base64

app = FastAPI()

@app.post("/process")
async def process(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # run ELA engine: returns (heatmap_bytes, score)
        heatmap_bytes, score = engine_ela.run_ela(contents)
        heatmap_b64 = base64.b64encode(heatmap_bytes).decode('utf-8')
        # optionally run AI model
        ai_result = engine_ai.analyze_image(contents)
        
        # Merge dicts to return flat structure
        response_data = {
            "heatmap_b64": heatmap_b64, 
            "ela_score": score
        }
        if ai_result:
            response_data.update(ai_result)
            
        return JSONResponse(response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
