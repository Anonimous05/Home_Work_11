from bs4 import BeautifulSoup
import requests

url = "https://24.kg"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
news = soup.find("div", {"class": "row lineNews"}).findChildren("div", {"class": "one"})


class Scrapper:
    def get_last_news(self):
        newsMass = []
        for i in news:
            time = i.find("div", {"class": "time"}).text
            title = i.find("div", {"class": "title"}).text
            link = i.find("a").attrs["href"]
            newsMass.append({"time": time, "title": title, "link": link})
        return newsMass

    def parse_detail_information(self, newsDetail):
        responseDetail = requests.get(url + newsDetail["link"]).text
        detailSoup = BeautifulSoup(responseDetail, "html.parser").find("div", {"class": "cont"}).text
        return detailSoup

    def get_html(self, url):
        responseHtml = requests.get(url).text
        soupHtml = BeautifulSoup(responseHtml, "html.parser")
        return soupHtml


newses = Scrapper().get_last_news()
details = Scrapper().parse_detail_information(newses[1])
html = Scrapper().get_html("https://google.com")
print(details)