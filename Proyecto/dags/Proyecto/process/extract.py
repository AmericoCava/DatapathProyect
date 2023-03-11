import os
from io import StringIO
from google.cloud.storage import Client
from azure.storage.blob import ContainerClient
import pandas as pd

class Extract():
    def __init__(self) -> None:
        self.process = 'Extract Process'

    def read_adls(self, containerName, fileName, name):
        
        conn_str = "BlobEndpoint=https://adlsdatapath.blob.core.windows.net/;QueueEndpoint=https://adlsdatapath.queue.core.windows.net/;FileEndpoint=https://adlsdatapath.file.core.windows.net/;TableEndpoint=https://adlsdatapath.table.core.windows.net/;SharedAccessSignature=sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-03-21T10:03:10Z&st=2023-02-22T02:03:10Z&spr=https,http&sig=thudqykpqiZUr2ty%2B%2B8HSkLvmQnb5ejHbMAr3YILHQ8%3D"
        container = containerName
        container_client = ContainerClient.from_connection_string(
            conn_str=conn_str, 
            container_name=container
        )
        downloaded_blob = container_client.download_blob(fileName)
        df = pd.read_csv(StringIO(downloaded_blob.content_as_text()), sep='|', header=None, index_col=None, names=name)
        return df

    def read_xml(self, path_file):
        df = pd.read_xml(path_file)
        return df