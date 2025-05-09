"""
This is a script for deleting resources in Azure DevOps.
"""

from pathlib import Path
import os, sys

classes_path = Path(Path(__file__).parent.parent.parent / 'classes')
sys.path.append(classes_path.resolve().as_posix())

from class_library import Library
from class_connection_service import ConnectionService
from class_logs import Logs

from dotenv import load_dotenv
import pandas as pd


# === Script configuration ===
devops_variable_group_name = 'ACR-SP-credentials' # Name of the Variable group which we will delete from DevOps Library
service_name = 'dataEngineeringApps' # Name of the Service connection which we will delete


# Load environment variables from the .env file
load_dotenv()


# === Deleting the Variable group ====
lib = Library(
    token = os.getenv('AZURE_DEVOPS_PAT')
    ,organization = os.getenv('DEVOPS_ORGANIZATION')
    ,project = os.getenv('DEVOPS_PROJECT')
)

lib.delete_variable_group(devops_variable_group_name)



# === Deleting the Service connection ===
conn_serv = ConnectionService(
    token = os.getenv('AZURE_DEVOPS_PAT')
    ,organization = os.getenv('DEVOPS_ORGANIZATION')
    ,project = os.getenv('DEVOPS_PROJECT')
)

conn_serv.delete_service(service_name)


# === Save logs about deleted resources ===
logs = Logs()

new_logs = pd.DataFrame([
        [devops_variable_group_name, 'Variable group', 'deleted']
        ,[service_name, 'Service connection', 'deleted']
    ]
    ,columns = ['resource_name', 'resource_type', 'action']
)

logs.add_logs(new_logs)
logs.save_logs()