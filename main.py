# Para ejecutar la app, puedes usar uvicorn, por ejemplo:
# uvicorn main:app --reload

from fastapi import FastAPI, Path, HTTPException
import datetime
import requests
import os
from dotenv import load_dotenv
import logging
from pydantic import BaseModel

from functions.crypto_functions import get_crypto_data, get_crypto
from functions.metro_functions import scrape_metro_status
from functions.miestacion_functions import miestacion
from functions.news_functions import noticias_economicas_español
from functions.stocks_functions import get_stock_price, allPrice
from functions.weather_functions import get_weather_data, weather_summary
from functions.checkprice_functions import product_sumary
from functions.aemet_functions import predict_weather

logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/crypto/{crypto}")
async def read_crypto(crypto: str = Path(None, description="The cryptocurrency you want to get data for")):
    try:
        logger.info(f"Getting data for {crypto}")
        return get_crypto_data(crypto)
    except Exception as e:
        logger.error(f"Error getting data for {crypto}: {e}")
        raise HTTPException(status_code=500, detail="Error getting data for {crypto}")
    

@app.get("/crypto/{crypto}/price")
async def read_crypto_price(crypto: str = Path(None, description="The cryptocurrency you want to get the price for")):
    try:
        logger.info(f"Getting price for {crypto}")
        return get_crypto(crypto)
    except Exception as e:
        logger.error(f"Error getting price for {crypto}: {e}")
        raise HTTPException(status_code=500, detail="Error getting price for {crypto}")
    
@app.get("/metro")
async def read_metro():
    try:
        logger.info("Getting metro status")
        return scrape_metro_status()
    except Exception as e:
        logger.error(f"Error getting metro status: {e}")
        raise HTTPException(status_code=500, detail="Error getting metro status")

@app.get("/miestacion")
async def read_miestacion():
    try:
        logger.info("Getting data from miestacion")
        return miestacion()
    except Exception as e:
        logger.error(f"Error getting data from miestacion: {e}")
        raise HTTPException(status_code=500, detail="Error getting data from miestacion")

@app.get("/news")
async def read_news():
    try:
        logger.info("Getting economic news in Spanish")
        return noticias_economicas_español()
    except Exception as e:
        logger.error(f"Error getting economic news in Spanish: {e}")
        raise HTTPException(status_code=500, detail="Error getting economic news in Spanish")

@app.get("/stocks/{url}/{company_name}")
async def read_stocks(url: str, company_name: str):
    try:
        logger.info(f"Getting stock price for {company_name}")
        return get_stock_price(url, company_name)
    except Exception as e:
        logger.error(f"Error getting stock price for {company_name}: {e}")
        raise HTTPException(status_code=500, detail="Error getting stock price for {company_name}")

@app.get("/stocks")
async def read_all_stocks():
    try:
        logger.info("Getting all stock prices")
        return allPrice()
    except Exception as e:
        logger.error(f"Error getting all stock prices: {e}")
        raise HTTPException(status_code=500, detail="Error getting all stock prices")

@app.get("/weather/{city}")
async def read_weather(city: str):
    try:
        logger.info(f"Getting weather data for {city}")
        return get_weather_data(city)
    except Exception as e:
        logger.error(f"Error getting weather data for {city}: {e}")
        raise HTTPException(status_code=500, detail="Error getting weather data for {city}")

@app.get("/weathersumary/{city}")
async def read_weather_summary(city: str):
    try:
        logger.info(f"Getting weather summary for {city}")
        return weather_summary(city)
    except Exception as e:
        logger.error(f"Error getting weather summary for {city}: {e}")
        raise HTTPException(status_code=500, detail="Error getting weather summary for {city}")

@app.get("/hora")
async def read_time():
    now = datetime.datetime.now()
    logger.info(f"Getting time")
    return {"hora": now.strftime("%H:%M:%S")}

@app.get("/fecha")
async def read_date():
    now = datetime.datetime.now()
    logger.info(f"Getting date")
    return {"fecha": now.strftime("%Y-%m-%d")}

@app.get("/dia")
async def read_datetime():
    now = datetime.datetime.now()
    logger.info(f"Getting date and time")
    return {"Dia": now.strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/checkprice/{product}")
async def read_product(product: str):
    try:
        logger.info(f"Getting price for {product}")
        return product_sumary(product)
    except Exception as e:
        logger.error(f"Error getting price for {product}: {e}")
        raise HTTPException(status_code=500, detail="Error getting price for {product}")
  
@app.get("/weatherprediction")
async def read_weather_prediction():
    try:
        logger.info("Getting weather prediction")
        return predict_weather()
    except Exception as e:
        logger.error(f"Error getting weather prediction: {e}")
        raise HTTPException(status_code=500, detail="Error getting weather prediction")