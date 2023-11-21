import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

# Exemplo de uso
upload_to_s3('meu_arquivo.csv', 'meu-bucket-s3')
