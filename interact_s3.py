import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

# s3_client.download_file("datalake-ney-igti",
#                         "data/Observabilidade.txt",
#                         "data/Observabilidade.txt")

# df = pd.read_csv("data/Observabilidade.txt", sep=";")
# print(df)

s3_client.upload_file("data/pnadc2020.csv",
                    "datalake-denissilva-589255375735",
                    "raw-data/pnadc2020.csv")
# s3_client.Bucket('datalake-denissilva-589255375735').upload_file('data/pnadc2020.csv', 'raw-data/pnadc2020.csv')