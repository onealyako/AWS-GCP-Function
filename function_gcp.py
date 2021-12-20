from google.cloud import storage

def copy_bucket_files():
    """
    Copies the files from a specified bucket into the selected one.
    """
    try:
        # Initiate Cloud Storage client
        storage_client = storage.Client()
        # Define the origin bucket
        origin = storage_client.bucket('oyako-a4')
        # Define the destination bucket
        destination = storage_client.bucket('oyako-a4-backup')

        # Get the list of the blobs located inside the bucket which files you want to copy
        blobs = storage_client.list_blobs('oyako-a4')

        for blob in blobs:
            origin.copy_blob(blob, destination)

        return "Done!"

    except:
        return "Failed!"


def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    copy_bucket_files()
