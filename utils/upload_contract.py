import shutil
import os

organization_name = input("Enter Organization Name: ")
source_file = input("Enter PDF File Path: ")

destination_folder = os.path.join(
    "database/organizations",
    organization_name
)

os.makedirs(destination_folder, exist_ok=True)

shutil.copy(source_file, destination_folder)
print("Contract uploaded successfully")