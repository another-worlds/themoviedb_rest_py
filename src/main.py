import requests
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

kek = "https://api.themoviedb.org/3/movie/550?api_key=316362573de67b3d7d1892fa8a6c4cc8"

project_dir = Path(__file__).parent.parent.resolve()
load_dotenv(os.path.join(project_dir, ".env"))

api_key = os.getenv("api_key")
api_version = os.getenv("api_version")

url_endpoint = "movie"
url_content_id = "550"
url_get_key = f"?api_key={api_key}"
url_base = f"https://api.themoviedb.org"

url = f"{url_base}/{api_version}/{url_endpoint}/{url_content_id}"

result = requests.get(url, params={"api_key":api_key})
print(result.json())
