from pathlib import Path
import os, sys

classes_path = Path(Path(__file__).parent.parent.parent / 'classes').resolve().as_posix()
sys.path.append(classes_path)

from dotenv import load_dotenv
import json

from class_connection_service import ConnectionService

# Load environment variables from the .env file
load_dotenv()

conn_serv = ConnectionService(
    token = os.getenv('AZURE_DEVOPS_PAT')
    ,organization = os.getenv('DEVOPS_ORGANIZATION')
    ,project = os.getenv('DEVOPS_PROJECT')
)

conn_serv.get_services()

print(json.dumps(conn_serv.conn_services, indent = 1))