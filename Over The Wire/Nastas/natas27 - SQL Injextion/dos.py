import requests
import re

url = "http://natas27.natas.labs.overthewire.org/index.php"
auth = ("natas27", "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3")  # Replace with the actual credentials


pattern = re.compile(r'\b[A-Za-z0-9]{32}\b')  # Regex pattern for 32-character alphanumeric code
excluded_code = "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"
for i in range(10000):
    