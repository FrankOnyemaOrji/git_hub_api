# This project we’re going to write a small program that requests the top repositories from GitHub,
# ordered by the number of stars each repository has
import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language: {language} "

        return query


def github_repo_api_stars(languages, sort="stars", order="desc"):
    api = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(api, params=parameters)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. Status code was: {status_code}")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = github_repo_api_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
