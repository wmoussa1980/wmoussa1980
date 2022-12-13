# This program will display title - artist - country - price - year based on input from cd_catalog.xml.
# #  References:
# #    Programming Fundamentals – 2nd Edition
# #    Professor Dave Braunschweig
# #    W3schools Python Tutorial
# #    stackoverflow.com
# #    www.geeksforgeeks.org

def read_file(filename, tags):
    try:
        with open(filename, "r") as file:
            array = []
            for line in file:
                line = line.strip()
                if line.endswith(tags[1]):
                    line = line.replace(tags[1], "")
                    line = line.replace(tags[0], "")
                    array.append(line)

            return array

    except Exception as exception:
        print(exception)


def calculate_average(price):
    total = 0
    for n in price:
        total = total + n
    average = total / len(price)
    return average


def display_items(price, title, artist, country, year, average):
    items = 0
    for item in range(len(title)):
        items = item + 1
        print(title[item] + ' - ' + artist[item]+' - ' + country[item], end = "")
        print(' - ' + str(price[item]) + ' - ' + year[item])
    print(items, 'items - ', "$%.2f" % average, 'average price ')


def main():
    filename = 'cd_catalog.xml'
    title_tag = ['<TITLE>', '</TITLE>']
    artist_tag = ['<ARTIST>', '</ARTIST>']
    prices_tag = ['<PRICE>', '</PRICE>']
    country_tag = ['<COUNTRY>', '</COUNTRY>']
    year_tag = ['<YEAR>', '</YEAR>']
    price = read_file(filename, prices_tag)
    title = read_file(filename, title_tag)
    artist = read_file(filename, artist_tag)
    country = read_file(filename, country_tag)
    year = read_file(filename, year_tag)
    average = calculate_average(price)
    display_items(price, title, artist, country, year, average)


main()
