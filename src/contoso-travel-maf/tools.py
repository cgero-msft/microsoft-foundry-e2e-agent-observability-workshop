"""Contoso Travel inventory search tools for the MAF agent."""
import os
import json
import pandas as pd
from typing import Annotated

# Load data relative to this file's location
_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
_flights_df = pd.read_csv(os.path.join(_DATA_DIR, "flights.csv"))
_hotels_df = pd.read_csv(os.path.join(_DATA_DIR, "hotels.csv"))
_cars_df = pd.read_csv(os.path.join(_DATA_DIR, "car_rentals.csv"))


def search_flights(
    origin: Annotated[str, "Departure city name"] = "",
    destination: Annotated[str, "Arrival city name"] = "",
    max_price: Annotated[float, "Maximum ticket price in USD"] = 10000,
) -> str:
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


def search_hotels(
    city: Annotated[str, "City name to search"] = "",
    min_stars: Annotated[int, "Minimum star rating (1-5)"] = 1,
    max_price: Annotated[float, "Maximum price per night in USD"] = 10000,
) -> str:
    """Search Contoso Travel hotel inventory by city, star rating, and nightly price."""
    results = _hotels_df.copy()
    if city:
        results = results[results["city"].str.lower().str.contains(city.lower())]
    results = results[results["star_rating"] >= min_stars]
    results = results[results["price_per_night_usd"] <= max_price]
    if results.empty:
        return json.dumps({"message": "No hotels found matching your criteria."})
    return results.head(5).to_json(orient="records", indent=2)


def search_car_rentals(
    city: Annotated[str, "Pickup city name"] = "",
    car_type: Annotated[str, "Vehicle type: Economy, SUV, Luxury, or Minivan"] = "",
) -> str:
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
