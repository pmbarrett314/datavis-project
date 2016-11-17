import asyncio
from io import BytesIO
import subprocess
import urllib.request
import xlsx2csv
import zipfile

@asyncio.coroutine
def get_aoa():

    url="http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip"

    with urllib.request.urlopen(url) as response:
        response_data=BytesIO(response.read())
    with zipfile.ZipFile(response_data) as aoa_zip:
        xlsx=aoa_zip.read("AoA_ratings_Kuperman_et_al_BRM.xlsx")

    csv=xlsx2csv.Xlsx2csv(BytesIO(xlsx))
    csv.convert("data/AoA_ratings_Kuperman_et_al_BRM.csv")

@asyncio.coroutine
def get_pos():
    url="http://concepticon.clld.org/parameters.csv?sEcho=1&iSortingCols=1&iSortCol_0=0&sSortDir_0=asc"
    with urllib.request.urlopen(url) as response, open("data/Parameters.csv", "wb") as out_file:
        response_data=response.read()
        out_file.write(response_data)

if __name__=="__main__":
    loop=asyncio.get_event_loop()
    tasks = [
    asyncio.ensure_future(get_aoa()),
    asyncio.ensure_future(get_pos())
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
