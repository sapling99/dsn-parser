"""
Objective is to print contents of 
https://eyes.nasa.gov/dsn/dsn.html in terminal.

1. fetch data from the website with requests
2. filter the appropriate data by creating a dictionary / array
3. print the appropriate data

1. go through isro exercises again.
2. to print just the antenna's details.
    - request this https://eyes.nasa.gov/dsn/config.xml - done
    - parse this to dictionary (how to parse xml?)
    - print location and corresponding antennas.
2.5. make a tree of temp.xml

"""
import requests
# this library parses xml into a ET class object
import xml.etree.ElementTree as ET

# r.text is generally in 'str' format. 
# one has to manually decide to convert into either array, or dictionary etc
r = requests.get("https://eyes.nasa.gov/dsn/config.xml")
data = r.text
print(type(data))


# three modes to 'open' a file, r, w, w+
# with open("temp.xml", "w") as ffile:
#     ffile.write(data)

"""
When we do json.loads, we give the json string as parameter
x = json.loads("{'a': 21}")
"""
# xmldata = ET.parse("temp.xml")
root = ET.fromstring(data)
print(root)

# we can iterate through children
"""
for child in root:
    print(child.tag)
"""
# or directly reference it like an array
sites = root[0]
spacecraft_map = root[1]
"""sites dictionary will be of the following format 
sitesDictionary = {
    "mdcc": [{"name": "DSS63", "friendlyName": "DSS 63", "type": "70M"}, {}, {}]
}
"""

sitesDictionary = {}
for site in sites:
    site_name = site.attrib["name"]
    sitesDictionary[site_name] = []
    """
    until this step, {'mdscc': [], 'gdscc': [], 'cdscc': []}
    is the result
    """
    for dish in site:
        dish_dict = {
            "name": dish.attrib["name"],
            "friendly_name": dish.attrib["friendlyName"],
            "type": dish.attrib["type"],
        }
        sitesDictionary[site_name].append(dish_dict)

print(sitesDictionary)


"""
Parse SpacecraftMap

spacecraftmap looks like an array of spacecraft.
spacecraft is a dictionary with keys:
    - name
    - explorerName
    - friendlyName
    - thumbnail
"""
spacecraft_map_arr = []
# run a for loop in spacecraft_map variable.


spacecraft_map_dictionary = {}
for spacecraft in spacecraft_map:
    spacecraftmap_name = spacecraft.attrib["name"]
    spacecraft_dict = {
        "name": spacecraft.attrib["name"],
        "explorer_name": spacecraft.attrib["explorerName"],
        "friendlyName": spacecraft.attrib["friendlyName"],
    }
    spacecraft_map_dictionary[spacecraftmap_name] = spacecraft_dict

print(type(spacecraft_map_dictionary))
print(spacecraft_map_dictionary["xmm"])


    
    
"""
for spacecraf in spacecraft_map:
        spacecraft_dict = {
            "name": spacecraf.attrib["name"],
            "explorer_name": spacecraf.attrib["explorerName"],
            "friendlyName": spacecraf.attrib["friendlyName"],
        }   
        spacecraft_map_arr.append(spacecraft_dict)
""" 
      
print(spacecraft_map_arr[0:2])

    