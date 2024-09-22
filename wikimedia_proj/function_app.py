import azure.functions as func
from azure.storage.blob import BlobServiceClient 
import logging
import requests
import json
import pandas as pd
import random 


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="wikimedia_rc")
@app.function_name("wikimedia_rc")
def wikimedia_rc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

# Above it, Boilerplate code
    streamUrl = "https://stream.wikimedia.org/v2/stream/recentchange"
    service_client = BlobServiceClient(
        account_url="https://wikimedia2.blob.core.windows.net/myfiles?sp=rw&st=2024-09-22T10:18:07Z&se=2024-09-23T18:18:07Z&sv=2022-11-02&sr=c&sig=GYpA6WvE2ELmR%2FooF3LqbXpr5MdTOcAl6MHK2RXoHP0%3D"
    )
    s = requests.Session()
    with s.get(streamUrl, stream=True) as resp:
        for line in resp.iter_lines(1024,decode_unicode=True):
            #Check if line has some bytes in it
            if line:
                #get the data lines only
                if line[:4] == "data":
                    json_line = json.loads(line[5:])
                    flatlines = pd.json_normalize(json_line, sep= "_")
                    file_name = "rc_"+str(random.randint(1,10000))+".json"
                    content = flatlines.to_json(orient="records", lines=True, index= False)
                    blob_client = service_client.get_blob_client(container = "myfiles",blob = file_name)
                    blob_client.upload_blob(content)
                    
    return func.HttpResponse
