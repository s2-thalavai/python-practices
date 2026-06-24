from fastapi import FastAPI

app = FastAPI()

def get_shipment():
    # Placeholder function to retrieve shipment details
    return {"shipment_id": 123, "status": "In Transit"} 

@app.get("/shipment/{shipment_id}")
def read_shipment(shipment_id: int):
    return get_shipment()       
