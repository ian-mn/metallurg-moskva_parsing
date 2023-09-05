import scrapy
from bs4 import BeautifulSoup
from metallurg_moskva.model import Row


class MetallurgMoskva(scrapy.Spider):
    name = "metallurg_moskva"
    allowed_domains = ["metallurg-moskva.ru"]
    start_url = "https://metallurg-moskva.ru/pricelist/"
    fields_mapping = {
        "Наименование": "name",
        "Диаметр": "diameter",
        "Марка": "brand",
        "price": "price",
        "measurement": "measurement",
        "Толщина, мм": "thickness",
        "Полка": "shelf",
        "Длина, мм": "length",
        "Размер": "size",
        "Ширина, мм": "width",
        "Стенка": "wall",
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_tables)

    def parse_items(self, tables) -> list[Row]:
        rows = []
        for table in tables:
            head = table.find("thead")
            headers = [x.text for x in head.find_all("th")]
            measurement = headers[-1].replace("Цена, ", "")
            headers[-1] = "price"

            for i, header in enumerate(headers):
                headers[i] = self.fields_mapping[header]

            body = table.find("tbody")
            trs = body.find_all("tr")

            for tr in trs:
                cells = tr.find_all("td")
                row = {k: v.text for k, v in zip(headers, cells)}
                row["measurement"] = measurement
                rows.append(Row(**row))
        return rows

    def parse_tables(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        price_list = soup.find("div", {"class": "pricelist-content"})
        tables = price_list.find_all("table")
        rows = self.parse_items(tables)
        yield from rows
