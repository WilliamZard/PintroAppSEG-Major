import os
from google.cloud import storage
import uuid

# TODO: consider movint this file into dedicated utils folder.


def upload_data_to_gcs(data: bytes) -> str:
    '''
        Function that store an image in a given bucket in GCP.
    '''
    '''Args:
        -bucket_name = the name of the GCP bucket where to store the image in.
        -data = an array of bytes rapresenting the image to store.
        
        Return:
        The public URL where the file is stored or an empty String if an exception occurs.

        Raise:
        A credentials related exceptions
    '''
    if len(data) > 0:  # If it is a string of length 0 abort the oreration. Otherwise it assumes data is bytes representing a file.
        try:
            # This will look for a GOOGLE_APPLICATION_CREDENTIALS env variable.
            client = storage.Client()
            bucket_name = os.environ.get('IMAGES_BUCKET_NAME')
            bucket = client.bucket(bucket_name)
            target_key = str(uuid.uuid4())  # unique file name in the bucket.
            bucket.blob(target_key).upload_from_string(data)
            return bucket.get_blob(target_key, timeout=150).public_url

        except Exception as e:
            print(e)

    return ''


def get_data_from_gcs(file_url: str) -> str:
    '''
        Function that gets a file stored in GCP buckets and returns a bytes object.
    '''
    '''Params:
        -bucket_name = the name of the GCP bucket where to look for the given file.
        -file_url = url for the file stored in GCP bucket that needs to be retrieved. 
        
        Return:
        A byte object that represents the retrieved file or an empty String  if an error 
        occurs or file_url is of length 0.
        
        Raise:
        A credentials related exceptions or an exception if the file is not found.
    '''
    if(len(file_url) > 0):
        try:
            # This will look for a GOOGLE_APPLICATION_CREDENTIALS env variable.
            client = storage.Client()
            bucket_name = os.environ.get('IMAGES_BUCKET_NAME')
            bucket = client.bucket(bucket_name)
            target_key = get_file_name_from_url(file_url)
            blob_json = bucket.get_blob(target_key, timeout=150).download_as_string(
                raw_download=True)  # get bucket data as blob
            return blob_json

        except Exception as e:
            print(e)

    return ''


def delete_data_from_gcs(file_url: str) -> str:
    '''
         Function that deletes a file stored in GCP buckets.
    '''
    '''Params:      
        -bucket_name = the name of the GCP bucket where to look for the given file.
        -file_url = url for the file stored in GCP bucket that needs to be deleted. 
        
        Raise:
        A credentials related exceptions or an exception if the file is not found.
    '''
    if(len(file_url) > 0):
        try:
            # This will look for a GOOGLE_APPLICATION_CREDENTIALS env variable.
            client = storage.Client()
            bucket_name = os.environ.get('IMAGES_BUCKET_NAME')
            bucket = client.bucket(bucket_name)
            target_key = get_file_name_from_url(file_url)
            bucket.delete_blob(target_key, timeout=150)
        except Exception as e:
            print(e)


def update_data_from_gcs(old_file_url: str, new_data: str) -> str:
    '''
        Function that update an image in a given bucket in GCP and returns its new url.
    '''
    '''Params:
        -bucket_name = the name of the GCP bucket where to store the image in.
        -old_file_url = url of the old file in GCP bucket that needs to be deleted from it.
        -new_data = new data in bytes that must be stored in a GCP bucket.
        
        Return:
        The public URL where the new file is stored or an empty String if an exception occurs.
        
        Raise:
        A credentials related exceptions or an exception if the file is not found.
    '''
    try:
        # This will look for a GOOGLE_APPLICATION_CREDENTIALS env variable.
        client = storage.Client()
        bucket_name = os.environ.get('IMAGES_BUCKET_NAME')
        bucket = client.bucket(bucket_name)
        # delete the previously stored file.
        if(len(old_file_url) > 0):
            old_target_key = get_file_name_from_url(old_file_url)
            bucket.delete_blob(old_target_key)
        # post the new file.
        # If it is a string of length 0 abort the oreration. Otherwise it assumes data is bytes representing a file.
        if(len(new_data) > 0):
            # unique file name in the bucket.
            new_target_key = str(uuid.uuid4())
            bucket.blob(new_target_key).upload_from_string(new_data)
            return bucket.get_blob(new_target_key, timeout=150).public_url

    except Exception as e:
        print(e)

    return ''


def clear_bucket() -> None:
    '''
        Function to clear all the existing files in a bucket.
    '''
    client = storage.Client()  # This will look for a GOOGLE_APPLICATION_CREDENTIALS env variable.
    bucket_name = os.environ.get('IMAGES_BUCKET_NAME')
    bucket = client.bucket(bucket_name)
    try:
        bucket.delete_blobs(blobs=bucket.list_blobs(), timeout=150)
    except Exception as e:
        print(e)


def get_file_name_from_url(file_url: str) -> str:
    return str(os.path.split(file_url)[1])
