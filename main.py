from google.cloud import bigquery


def load_bq(request):
    # Construct a BigQuery client object.
    client = bigquery.Client()
    table_id = "utility-cumulus-372111.json_loads.fruit_load"
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("fruit", "STRING"),
            bigquery.SchemaField("size", "STRING"),
            bigquery.SchemaField("color", "STRING"),

        ],
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )

    uri = "gs://sample-json-files/fruits.json"

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        location="europe-north1",  # Must match the destination dataset location.
        job_config=job_config,
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))

 
    return "success"