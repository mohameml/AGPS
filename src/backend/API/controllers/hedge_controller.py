import traceback
from fastapi import APIRouter, HTTPException , Depends

from backend.API.models.PortfolioDataRequest import PortfolioDataRequest
from backend.HedgingEngine.Portfolio.PortfolioData import PortfolioData
from backend.instances import get_hedge_engine

router = APIRouter()


@router.post("/hedge")
async def hedge(portfolio_data: PortfolioDataRequest , hedge_engine = Depends(get_hedge_engine)):
    try:
        portfolioData = PortfolioData(
            cash=portfolio_data.cash,
            compos=portfolio_data.compos,
            date=portfolio_data.date,
            isFirstTime=portfolio_data.isFirstTime
        )
        date = portfolio_data.currDate
        
        output , portfolio = hedge_engine.hedge(date , portfolioData)
        res = {
            "status": "success",
            "data" : {
                "output": output,
                "portfolio": portfolio
            }
        }

        return res
    except Exception as e:
        print(traceback.print_exc())
        
        raise HTTPException(status_code=500, detail=str(e))