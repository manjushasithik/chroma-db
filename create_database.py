

import subprocess

# Uninstall old version
subprocess.run(['pip', 'uninstall', 'sqlite3', '-y'])

# Install latest version
subprocess.run(['pip', 'install', 'sqlite3'])
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
print("SQLite updated successfully.")
import sqlite3
from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import yaml
############################################### from data_loader import load_text


# load the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# create the open-source embedding function
def create_vector_db(container_name):
    embedding_function = SentenceTransformerEmbeddings(model_name=config['Model'])
    #data_text = load_text(config['Containers'][f'{container_name}'])
    data_text = ["abscccc","dddfdfdf"]
    vector_db =Chroma.from_texts(data_text, persist_directory="db/", embedding=embedding_function)
                     
    #vector_db = Chroma.from_documents(documents=data_text, persist_directory="db/", embedding=embedding_function)
    return True


