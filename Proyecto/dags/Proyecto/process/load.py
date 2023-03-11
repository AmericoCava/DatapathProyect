import io
import os
from io import StringIO
from azure.storage.blob import ContainerClient
from google.cloud.storage import Client
import pandas as pd
from process.util import utils as u


class Load():
    def __init__(self) -> None:
        self.process = 'Load Process'

    def load_to_adls(self, df, containerName, blobName):

        conn_str = "BlobEndpoint=https://adlsdatapath.blob.core.windows.net/;QueueEndpoint=https://adlsdatapath.queue.core.windows.net/;FileEndpoint=https://adlsdatapath.file.core.windows.net/;TableEndpoint=https://adlsdatapath.table.core.windows.net/;SharedAccessSignature=sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-03-21T10:03:10Z&st=2023-02-22T02:03:10Z&spr=https,http&sig=thudqykpqiZUr2ty%2B%2B8HSkLvmQnb5ejHbMAr3YILHQ8%3D"
        container = containerName
        container_client = ContainerClient.from_connection_string(
            conn_str=conn_str, 
            container_name=container
        )
        output = io.StringIO()
        output = df.to_csv(encoding = "utf-8", index=False)
        container_client.upload_blob(blobName, output, overwrite=True, encoding='utf-8')
    
    def load_mysql(self, df, db_tbl_name):
        
        u.df_to_mysql(df, u.mysql_engine(), db_tbl_name)