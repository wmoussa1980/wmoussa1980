# This program will display xml file content based on input from plant_catalog.xml.
# #  References:
# #    Programming Fundamentals – 2nd Edition
# #    Professor Dave Braunschweig
# #    W3schools Python Tutorial
# #    stackoverflow.com
# #    www.geeksforgeeks.org

import os


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
    except FileNotFoundError:
        print("")


def calculate_average(price):

    total = 0
    for n in price:
        total = total + n
    average = total / len(price)
    return average


def display_items(price, common, botanical, light, zone, average):
    items = 0
    for item in range(len(common)):
        items = item + 1
        print(common[item] + ' ('+botanical[item] + ')' + ' - ', end = "")
        print(light[item] + ' - ' + zone[item] + ' -$ ' + str(price[item]))
    print(items, 'items - ', "$%.2f" % average, 'average price ')


def error_handling(filename):
    if os.path.getsize('plant_catalog.xml') == 0:
        print("File is empty")
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
        return line
    except FileNotFoundError:
        print("File is missing")
    except ValueError:
        print("Error: Missing or bad data.")
    except TypeError:
        print("Error: Missing or bad data.")


def main():
    filename = 'plant_catalog.xml'
    error_handling(filename)
    common_tag = '<COMMON>', '</COMMON>'
    zone_tag = '<ZONE>', '</ZONE>'
    prices_tag = '<PRICE>$', '</PRICE>'
    botanical_tag = '<BOTANICAL>', '</BOTANICAL>'
    light_tag = '<LIGHT>', '</LIGHT>'
    price = read_file(filename, prices_tag)
    price = [float(i) for i in price]
    common = read_file(filename, common_tag)
    zone = read_file(filename, zone_tag)
    botanical = read_file(filename, botanical_tag)
    light = read_file(filename, light_tag)
    average = calculate_average(price)
    display_items(price, common, botanical, zone, light, average)


main()
