# THis file is setting up a class for using S3Boto3Storage (storing static media files in S3 bucket) 

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False