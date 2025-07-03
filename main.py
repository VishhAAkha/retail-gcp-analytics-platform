def hello_gcs(event, context):
    import base64
    import json
    import logging

    bucket = event['bucket']
    name = event['name']
    logging.info(f"File uploaded: {name} in bucket {bucket}")

    # This is a placeholder for your real ETL logic
    print(f"Triggered by file: {name} in bucket: {bucket}")
