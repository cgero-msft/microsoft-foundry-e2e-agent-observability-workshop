"""Contoso Travel inventory search tools for the LangGraph agent."""
import os
import json
import pandas as pd
from langchain_core.tools import tool

# Load data relative to this file's location
_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
_flights_df = pd.read_csv(os.path.join(_DATA_DIR, "flights.csv"))
_hotels_df = pd.read_csv(os.path.join(_DATA_DIR, "hotels.csv"))
_cars_df = pd.read_csv(os.path.join(_DATA_DIR, "car_rentals.csv"))


@tool
def search_flights(origin: str = "", destination: str = "", max_price: float = 10000) -> str:
    """Search Contoso Travel flight inventory by origin, destination, and price."""
    results = _flights_df.copy()
    if origin:
        results = results[results["origin"].str.lower().str.contains(origin.lower())]
    if destination:
        results = results[results["destination"].str.lower().str.contains(destination.lower())]
    results = results[results["price_usd"] <= max_price]
    if results.empty:
        return json.dumps({"message": "No flights found matching your criteria."})
    return results.head(5).to_json(orient="records", indent=2)


@tool
def search_hotels(city: str = "", min_stars: int = 1, max_price: float = 10000) -> str:
    """Search Contoso Travel hotel inventory by city, star rating, and nightly price."""
    results = _hotels_df.copy()
    if city:
        results = results[results["city"].str.lower().str.contains(city.lower())]
    results = results[results["star_rating"] >= min_stars]
    results = results[results["price_per_night_usd"] <= max_price]
    if results.empty:
        return json.dumps({"message": "No hotels found matching your criteria."})
    return results.head(5).to_json(orient="records", indent=2)


@tool
def search_car_rentals(city: str = "", car_type: str = "") -> str:
    """Search Contoso Travel car rental inventory by city and vehicle type."""
    results = _cars_df.copy()
    if city:
        results = results[results["city"].str.lower().str.contains(city.lower())]
    if car_type:
        results = results[results["car_type"].str.lower() == car_type.lower()]
    results = results[results["available"]]
    if results.empty:
        return json.dumps({"message": "No car rentals found matching your criteria."})
    return results.head(5).to_json(orient="records", indent=2)
