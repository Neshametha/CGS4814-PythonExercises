import main_functions
import requests

url= "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosty/photos?sol=1000&api_key="

nasa_api_dict = main_functions.read_from_file("nasa_api.json")
my_api_key = nasa_api_dict["nasa_api"]

url2 = url + my_api_key
