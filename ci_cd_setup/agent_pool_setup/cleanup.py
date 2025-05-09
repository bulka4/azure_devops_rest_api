"""
This script is deleting a given Agent pool.
"""

from pathlib import Path
import os, sys

classes_path = Path(Path(__file__).parent.parent.parent / 'classes')
sys.path.append(classes_path.resolve().as_posix())

from class_agent_pool import AgentPool
from class_logs import Logs

from dotenv import load_dotenv
import pandas as pd


# === Script configuration
pool_name = 'data_engineering_apps'



# Load environment variables from the .env file
load_dotenv()

pool = AgentPool(
    token = os.getenv('AZURE_DEVOPS_PAT')
    ,organization = 'mbulka44'
    ,project = 'data_engineering'
)

pool.delete_agent_pool(pool_name)



# === Save logs about deleted agent ===
logs = Logs()
new_logs = pd.DataFrame(
    [[pool_name, 'deleted']]
    ,columns = ['pool_name', 'action']
)
logs.add_logs(new_logs)
logs.save_logs()