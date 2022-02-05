import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
# from datetime import date

collection = []


# CHRIS - JOSÉ - RUI - PEDRO - IVO - LOBO
authors_id = ["-HHz0G8AAAAJ", "U_E1voQAAAAJ",
              "_SvK39MAAAAJ", "r_NZkGUAAAAJ", "-7DehO8AAAAJ", "8cTP_acAAAAJ" ]


def checkKey(dict, key):
    if key in dict.keys():
        return True
    return False


def write_to_file():
    file_object = open("reference.bib", "a+")
    file_object.truncate(0)
    for index, article in enumerate(collection):
        file_object.write("@article{A" + str(index) + ",\r\n")
        if checkKey(article, "authors"):
            file_object.write(
                " author={" + (article['authors'].replace(", ...", "")).replace(",", " and ") + "},\r\n")
        if checkKey(article, "title"):
            file_object.write(" title={" + article['title'] + "},\r\n")
        # file_object.write(" journal={" + article['authors'] + "},\r\n")
        if checkKey(article, "year"):
            file_object.write(" year={" + article['year'] + "},\r\n")
        if checkKey(article, "publication"):
            file_object.write(
                " journaltitle={" + article['publication'].replace("...", "") + "},\r\n")
        file_object.write("}\r\n")


def check_already_exist(title):
    for a in collection:
        if title == a['title']:
            return True
    return False


def main():
    # todays_date = date.today()
    # year = todays_date.year-10
    params = {
        "engine": "google_scholar_author",
        # "as_ylo": "2012",
        "num": "30",
    }
    params["api_key"] = os.getenv('api_key')

    for author in authors_id:
        params.pop("author_id", None)
        params["author_id"] = author

        search = GoogleSearch(params)
        results = search.get_dict()
        articles = results['articles']
        for jsonArticle in articles:
            if not check_already_exist(jsonArticle['title']):
                collection.append(jsonArticle)
                # print(jsonArticle)

    if len(collection) > 0:
        write_to_file()


if __name__ == "__main__":
    load_dotenv()
    main()
