from fastapi import FastAPI

app = FastAPI()

def get_shipment(shipment_id: int):
    # Placeholder function to retrieve shipment details
    return {"shipment_id": shipment_id, "status": "In Transit"} 

@app.get("/shipment/{shipment_id}")
def read_shipment(shipment_id: int):
    return get_shipment(shipment_id)       
