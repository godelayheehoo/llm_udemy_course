import os
import requests


def scraped_linkedin_profile(linked_profile_url: str):
    """
    scrape information from linkedin profiles,
    Manually scrape the information from the linkedin profile
    """
    git_gist_url = "https://gist.githubusercontent.com/godelayheehoo/bde7ce8c6af93cadc82ff99ba3a6fdef/raw/50044287288168ea513f5fff784227cdc0dfd611/ede-marco.json"
    response = requests.get(git_gist_url)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
