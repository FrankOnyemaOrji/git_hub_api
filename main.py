# This project we’re going to write a small program that requests the top repositories from GitHub,
# ordered by the number of stars each repository has
import requests


def create_query(languages, min_stars=50000):
    query = f"Stars: > {min_stars} "

    for lan in languages:
        query += f"languages: {lan}"

        return query


def github_repo_api_stars(language, sort="stars", orders="desc"):
    api = "https://api.github.com/search/repositories"

    query = create_query(language)
    param = {"q": query, "sort": sort, "order": orders}
    response = requests.get(api, params=param)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. Status code was: {status_code}")
    else:
        response_json = response.json()
        return response_json["items"]


if __name__ == "__main__":
    languagess = ["python", "javascript", "ruby"]
    results = github_repo_api_stars(languagess)

    for result in results:
        language_s = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language_s} repo with {stars} Stars.")
