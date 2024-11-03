from http import HTTPStatus

from fastapi import APIRouter

from service.price_service import PriceService

router = APIRouter()



@router.get("/{gold_price}/{silver_price}/{bronze_price}")
def get(gold_price: int, silver_price: int, bronze_price: int):
    return PriceService.get_price(gold_price, silver_price, bronze_price)