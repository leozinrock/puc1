import requests


def download(url, arquivo):
    response = requests.get(url + arquivo, headers={"User-Agent": "XY"})
    open(arquivo, "wb").write(response.content)
