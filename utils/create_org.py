import os

organization_name = input("Enter Organization Name: ")

base_path = "database/organizations"

org_folder = os.path.join(base_path, organization_name)

os.makedirs(org_folder, exist_ok=True)

print(f"Folder created successfully: {org_folder}")