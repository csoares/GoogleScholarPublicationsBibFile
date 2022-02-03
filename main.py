import os
from operator import truediv
from serpapi import GoogleSearch
from dotenv import load_dotenv

collection = []


# CHRIS - JOSÉ - RUI - PEDRO
authors_id = ["-HHz0G8AAAAJ", "U_E1voQAAAAJ", "_SvK39MAAAAJ", "r_NZkGUAAAAJ"]


def write_to_file():
    print("test")
    file_object = open("reference.bib", "a+")
    file_object.truncate(0)
    for index, article in enumerate(collection):
        file_object.write("@article{A" + str(index) + ",\r\n")
        file_object.write(
            " author={" + (article['authors'].replace("...", "")).replace(",", " and ") + "},\r\n")
        file_object.write(" title={" + article['title'] + "},\r\n")
        # file_object.write(" journal={" + article['authors'] + "},\r\n")
        file_object.write(" year={" + article['year'] + "},\r\n")
        file_object.write(
            " journaltitle={" + article['publication'] + "},\r\n}\r\n")


def check_already_exist(title):
    for a in collection:
        if title == a['title']:
            return True
    return False


def main():

    for author in authors_id:

        params = {
            "engine": "google_scholar_author",
        }
        params["author_id"] = author
        params["api_key"] = os.getenv('api_key')

        search = GoogleSearch(params)
        results = search.get_dict()
        articles = results['articles']

        for jsonArticle in articles:
            if not check_already_exist(jsonArticle['title']):
                collection.append(jsonArticle)
                print(jsonArticle)

    if len(collection) > 0:
        write_to_file()


if __name__ == "__main__":
    load_dotenv()
    main()
