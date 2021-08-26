from bs4 import BeautifulSoup
import requests
import csv

place_holder = []
initial_url = input('Enter target website: \n')


def scrape_func(url):
    if url not in place_holder:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for thing in soup.find_all("a"):
            x = thing.get('href')
            if x not in place_holder:
                place_holder.append(url + x)


scrape_func(initial_url)
for i in place_holder:
    scrape_func(i)


fields = ['scrapped URL']
rows = place_holder
file_name = "test.csv"

with open(file_name, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerow(rows)


print(place_holder)
length = len(place_holder)
print(length)
