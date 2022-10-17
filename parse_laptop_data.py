

"""
Below is a dictionary of the top 2 laptops of 2020 as reviewed by Tech Crunch.

This data was pulled from an API. Currently there is no Python version of this API to use,
so the data has been ported in as is.

Our goal is to be able to parse this data with code, so that we can utilize it in our code.
"""

laptops = [
        {
            "id": "1",
            "productName": "Apple Macbook Pro",
            "url": "https://www.apple.com/macbook-pro-13/",
            "types": [
                {
                    "id": "1",
                    "screen_size": "13-inch",
                    "cpu": ["1.4GHz quad-core 8th-generation Intel Core i5 processor", "2.0GHz quad-core 10th-generation Intel Core i5 processor"],
                    "ram": ["8GB","16GB"],
                    "storage": ["256GB SSD","512 GB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [1299, 1499, 1799]
                },
                {
                    "id": "2",
                    "screen_size": "16-inch",
                    "cpu": ["2.6GHz 6-core 9th-generation Intel Core i7 processor", "2.3GHz 8-core 9th-generation Intel Core i9 processor"],
                    "ram": ["16GB"],
                    "storage": ["512 GB SSD", "1 TB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [2399, 2799]
                }
            ],
            "description": "If you're after the latest and greatest laptop from Apple, we suggest you look into the 2020 model of the MacBook Pro. The headline Touch Bar – a thin OLED display at the top of the keyboard which can be used for any number of things, whether that be auto-suggesting words as you type or offering Touch ID so you can log in with just your fingerprint – is of course included. It's certainly retained Apple's sense of style, but it comes at a cost. This is a pricey machine, so you may want to consider one of the Windows alternatives. But, if you're a steadfast Apple diehard, this is definitely the best laptop for you!"
        },
        {
            "id": "2",
            "productName": "Dell XPS",
            "url": "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps-laptops?~ck=bt",
            "types": [
                {
                    "id": "3",
                    "screen_size": "13-inch",
                    "cpu": ["11th Generation Intel Core i3-1115G4 Processor", "11th Generation Intel Core i5-1135G7 Processor"],
                    "ram": ["8GB"],
                    "storage": ["256GB SSD","512 GB SSD", "1 TB SSD"],
                    "colors": ["Platinum silver exterior, black interior", "Platinum silver exterior, black interior"],
                    "price": [999, 1099, 1149, 1249]
                },
                {
                    "id": "4",
                    "screen_size": "15-inch",
                    "cpu": ["10th Generation Intel Core i5-10300H"],
                    "ram": ["8GB", "16GB", "32GB", "64GB"],
                    "storage": ["256 GB SSD", "512 GB SSD", "1 TB SSD", "2 TB SSD"],
                    "colors": ["Frost White with White Palmrest", "Frost White with White Palmrest"],
                    "price": [1199, 1299, 1399, 1749, 1999, 2299]
                }
            ],
            "description": "The Dell XPS is an absolutely brilliant laptop. The 2020  version rocks an 11th-generation Intel Core i3, i5 or i7 processor and a bezel-less 'Infinity Edge' display. This Dell XPS continues to be the most popular Windows laptop in the world. What's more, there's a wide range of customization options, so you can really make the Dell XPS the best laptop for your needs. "
        }
]


# 1.1 TODO: Print out the MacBook Pro url


# 1.2 TODO: Write a function called `print_laptop_data` that takes in two parameters: `laptop` and `topic`, and returns nothing.
#
#   If `laptop` is 'Apple Macbook Pro', the function should print out data about that computer.
#   If `laptop` is 'Dell XPS', the function should print out data about that computer.
#
#   NOTE: There are multiple types of each computer. Assume the user wants to know about the ones with
#       the smaller (and therefore cheaper) screen size.
#
#   The `topic` can be anything about the type of computer (price, screen size, cpu, etc). For example:
#   If `topic` is 'prices', the function should print out all possible prices of the specified computer.
#   If `topic` is 'colors', the function should print out all possible colors of the specified computer.
#   etc etc etc for each computer topic. (NOTE: you do NOT need an if- or elif- statement for each option.)
#
#   The data should print out like so:
#   <computer-name> <topic>: <data>
#
#   So, for instance:
#   Dell XPS ram: ["8GB", "16GB", "32GB", "64GB"]


# 1.3 TODO: Call your function 3 times to print out:
#   1.3.1: All possible prices of the Apple Macbook Pro.
#   1.3.2: All the color options for the Dell XPS.
#   1.3.3: The screen_size of the Dell XPS.


# 2.1 TODO: Write a function called `list_prices` that takes one parameter: a list of computers, and returns nothing.
#   Using nested loops, the function should print out all possible computer prices, one price on each line.
#   No need to specify which computer each price belongs to.


# 2.2 TODO: Call your function to see that it works.


# 3.0 Suppose that the two versions of the 16-inch MacBook Pro are no longer available:
#   - In the color 'space gray'
#   - With '1 TB SSD' storage

# 3.1 TODO: Update the `laptops` dictionary to reflect these changes.


# 3.2 TODO: Print out the Macbook Pro dictionary to see the changes.


# BONUS TODO: Write a function called `get_price_range` that returns the minimum and maximum prices out of all the options.

# ^ Expected outcome: (999, 2799)