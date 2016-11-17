from io import BytesIO
import subprocess
import urllib.request
import xlsx2csv
import zipfile

url="http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip"

with urllib.request.urlopen(url) as response:
    response_data=BytesIO(response.read())
with zipfile.ZipFile(response_data) as aoa_zip:
    xlsx=aoa_zip.read("AoA_ratings_Kuperman_et_al_BRM.xlsx")

csv=xlsx2csv.Xlsx2csv(BytesIO(xlsx))
csv.convert("data/AoA_ratings_Kuperman_et_al_BRM.csv")

