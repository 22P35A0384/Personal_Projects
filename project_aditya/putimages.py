import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('21p31a0224.jpg','21p31a0224')]

# Iterate through list to upload objects to S3   
for image in images:
    file = open('main_images/'+image[0],'rb')
    object = s3.Object('mobileapppp','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
