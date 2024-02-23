from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from bs4 import BeautifulSoup
from pydantic import BaseModel
from rag_app import index

class InputText(BaseModel):
    text: str

app = FastAPI() 
xml_file_path = "test.xml"

# Endpoint to read and return the XML file
@app.get("/xml")
async def read_xml():
    try:
        with open(xml_file_path, 'mr') as f:
            data = f.read()
        print(data)
        bs_data = BeautifulSoup(data, "xml")
        xml_content = bs_data.prettify()

        return PlainTextResponse(content=xml_content, media_type="application/xml")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="XML file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
@app.get("/")
async def root():
    return {'app':'bot'}

@app.post("/chat")
async def process_text(input_text: str):
    try:
        result = index(input_text)
        return {"result": result.response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
