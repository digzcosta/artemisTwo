# Integration layer with the Adzuna API. 
# Returns raw data on job vacancies.

import requests
from src.config import adzuna_app_id, adzuna_app_key
from src.logger import log

base_url = "https://api.adzuna.com/v1/api/jobs"

def search_jobs(term: str, page: int = 1, country: str = "br") -> dict | None:
    
    url = f"{base_url}/{country}/search/{page}"
    
    params = {
        "app_id": adzuna_app_id,
        "app_key": adzuna_app_key,
        "what": term
    }

    log.info("Requesting Adzuna: term={} page={}", term, page)
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        log.debug("Adzuna returned {} results", len(data.get("results", [])))
        return data
    
    except requests.exceptions.RequestException as e:
        log.exception("Adzuna request failed.")
        return None