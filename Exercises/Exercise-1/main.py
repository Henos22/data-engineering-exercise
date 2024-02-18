import requests
from io import BytesIO
import os 
import pandas as pd
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_downloads_directory_if_not_exists() -> None:

    directory = "Downloads"
    parent_directory = "/Users/henostsegai/work/data-engineering-exercise/Exercises"

    if os.path.isdir(f"{parent_directory}/{directory}"):

        print("Downloads directory already exists")
        return
    
    path = os.path.join(parent_directory, directory)
    return os.mkdir(path)

def download_csvs_from_zip_files():

    for url in download_uris[:1]:

        csv_file_name = f"{url.split('/')[-1][:-3]}csv"
        print("csv file name: ",csv_file_name)

        try:

            filename = requests.get(url).content
            zf = ZipFile( BytesIO(filename), 'r' )

            for filename in zf.namelist():

                print("File in zip: "+ filename)

                if csv_file_name == filename:

                    df = pd.read_csv( zf.open(filename), encoding="latin-1")
                    df.to_csv(path_or_buf=f"/Users/henostsegai/work/data-engineering-exercise/Exercises/Downloads/{csv_file_name}")
        except:

            print(f"The following url is not valid: {url}")
    return

def main():
    create_downloads_directory_if_not_exists()
    download_csvs_from_zip_files()
    pass


if __name__ == "__main__":
    main()
