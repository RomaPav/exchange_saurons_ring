import asyncio
from http import HTTPStatus

from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from service.price_service import PriceService

router = APIRouter()



@router.get("/{gold_price}/{silver_price}/{bronze_price}")
def get(gold_price: int, silver_price: int, bronze_price: int):
    return PriceService.get_price(gold_price, silver_price, bronze_price)

@router.websocket("/ws/price")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    gold_price = 0
    silver_price = 0
    bronze_price = 0
    try:
        while True:
            prices = PriceService.get_price(gold_price, silver_price, bronze_price)

            await websocket.send_json(prices)

            gold_price = prices["gold"]
            silver_price = prices["silver"]
            bronze_price = prices["bronze"]

            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("Client disconnected")