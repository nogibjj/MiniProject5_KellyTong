import requests

def extract(
    url="https://github.com/nogibjj/MiniProject5_KellyTong/blob/main/Auto.csv", 
    file_path="Auto.csv"
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
