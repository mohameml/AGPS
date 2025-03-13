from fastapi import APIRouter, HTTPException , Depends
from backend.instances import   get_market_data_reader
from backend.API.models.NextDayRequest import NextDayRequest


router = APIRouter()



@router.get("/next-day/")
async def get_data_feed(next_day_req: NextDayRequest , market_data_reader=Depends(get_market_data_reader)):
    try:
        date = next_day_req.date
        feed = market_data_reader.get_data_feed(date)
        res = {
            "status": "success",
            "data" : {
                "date": feed.date,
                "dict_index_price": feed.dict_index_price,
                "dict_exchange_rate": feed.dict_exchange_rate
            }
        }
        return res 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))