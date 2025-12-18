from datetime import datetime


def cleaning_dict_jobs(job_json):
    return {
        "external_id": job_json.get("id"),
        "title": job_json.get("title"),
        "company": job_json.get("company", {}).get("display_name", "Anonymous"),
        "location": job_json.get("location", {}).get("display_name"),
        "salary": None,
        "created_at": datetime.fromisoformat(
            job_json.get("created", "").replace("Z", "")
        ) if job_json.get("created") else None,
        "url": job_json.get("redirect_url"),
    }
