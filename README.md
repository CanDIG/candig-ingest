CanDIG-ingest
==============

A Python package for batch ingestion and update of clinical and pipeline metadata of candig-server.

For more information related to the setup of a candig-server instance, check out https://candig-server.readthedocs.io/

You may also refer to the SETUP.rst at this repo, from https://github.com/CanDIG/candig-ingest/blob/develop/setup.py

## Get started

This tool is not for standalone use. You must have an existing virtual environment where a candig-server is installed.

Once you are in the virtual environment of where your candig-server is, activate it, and run

.. code:: bash
      pip install candig-ingest

## Prepare data for ingestion

Once the package is installed, you may batch ingest or update data. The candig-ingest requires a specially-formatted json file for this purpose.
This page describes the format of the data: https://candig-server.readthedocs.io/en/stable/data.html#clinical-and-pipeline-metadata

To help you get started quicker, we provide a few sample json files that are ready to use, you may retrieve them from https://github.com/CanDIG/candig-ingest/tree/develop/candig/ingest/mock_data

Alternatively, if you need to export data from RedCap APIs, we provide a conversion script that is available from https://github.com/CanDIG/redcap-cloud

## Ingest data

```
Usage:
  ingest [-h Help] [-v Version] [-d Description] [--overwrite] <path_to_database> <dataset_name> <metadata_json>
```

As you can see from above, the `ingest` command only has 3 mandatory parameters.

Assume we download a mock data file from the github repo linked above, and you have your candig-server's virtualenv activated, you will need to 

.. code:: bash
      wget https://raw.githubusercontent.com/CanDIG/candig-ingest/develop/candig/ingest/mock_data/clinical_metadata_tier1.json
      ingest candig-example-data/registry.db mock1 clinical_metadata_tier1.json -d "A collection of data from Mars"
      

You may see some warning messages that say "Skipped: Missing 1 or more primary identifiers for record ..." if you use the mock data, this is normal. 
We designed the mock data to be faulty on purpose. For production data, however, you should not see this message.

If you want to add a text description to your dataset, you should use the `-d` flag, note that the description cannot be updated at this time once 
the dataset is created. This is optional, however.

## Update data

Assume you have data ingested to a database's dataset already, and would like to update them in batch. 

If this applies to you, you should specify the `--overwrite` flag, this will update all records.

If you do not see specify this flag, the system will warn you that a record with the same identifier exists.

.. code:: bash
      ingest candig-example-data/registry.db mock1 updated_data.json --overwrite

Note that the description of the dataset cannot be changed once it's created, so a `-d` flag won't do anything.

## Questions and comments

Please open an issue here and let us know!