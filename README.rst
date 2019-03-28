==============
CanDIG-ingest
==============

Routines for ingesting metadata into a CanDIG 1.0 server
Requires `ga4gh-server
<https://github.com/ga4gh/ga4gh-server>`_
 `docopt
<http://docopt.readthedocs.io/en/latest/>`_
and `pandas <https://github.com/pandas-dev/pandas>.

* Free software: GNU General Public License v3


You can run the ingestion and test a server with the resulting repo as follows 
(requires Python 2.7 for the candig server)

.. code:: bash

    # Install
    virtualenv test_server
    cd test_server
    source bin/activate
    pip install --upgrade pip setuptools
    pip install git+https://github.com/CanDIG/candig-schemas.git@develop#egg=ga4gh_schemas
    pip install git+https://github.com/CanDIG/candig-client.git@authz#egg=ga4gh_client
    pip install git+https://github.com/CanDIG/candig-server.git@develop#egg=ga4gh_server
    pip install git+https://github.com/CanDIG/candig-ingest.git@master#egg=PROFYLE_ingest

    # setup initial peers
    mkdir -p ga4gh/server/templates
    touch ga4gh/server/templates/initial_peers.txt

    # ingest data and make the repo
    mkdir ga4gh-example-data
    ingest ga4gh-example-data/registry.db <path to example data, like: mock_data/clinical_metadata_tier1.json>

    # optional
    # add peer site addresses
    ga4gh_repo add-peer ga4gh-example-data/registry.db <peer site IP address, like: http://127.0.0.1:8001>

    # optional
    # create dataset for reads and variants
    ga4gh_repo add-dataset --description "Reads and variants dataset" ga4gh-example-data/registry.db read_and_variats_dataset

    # optinal
    # add reference set, data source: https://www.ncbi.nlm.nih.gov/grc/human/ or http://genome.wustl.edu/pub/reference/
    ga4gh_repo add-referenceset ga4gh-example-data/registry.db <path to downloaded reference set, like GRCh37-lite.fa> -d "GRCh37-lite human reference genome" --name GRCh37-lite --sourceUri "http://genome.wustl.edu/pub/reference/GRCh37-lite/GRCh37-lite.fa.gz"

    # optional
    # add reads
    ga4gh_repo add-readgroupset -r -I <path to bam index file> -R GRCh37-lite ga4gh-example-data/registry.db read_and_variats_dataset <path to bam file>

    # optional
    # add variants
    ga4gh_repo add-variantset -I <path to variants index file> -R GRCh37-lite ga4gh-example-data/registry.db read_and_variats_dataset <path to vcf file>
    
    # optional
    # add sequence ontology set
    # wget https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/so.obo
    ga4gh_repo add-ontology ga4gh-example-data/registry.db <path to sequence ontology set, like: so.obo> -n so-xp

    # optional
    # add features/annotations
    #
    ## get the following scripts
    # https://github.com/ga4gh/ga4gh-server/blob/master/scripts/glue.py
    # https://github.com/ga4gh/ga4gh-server/blob/master/scripts/generate_gff3_db.py
    #
    ## download the relevant annotation release from Gencode
    # https://www.gencodegenes.org/releases/current.html
    #
    ## decompress
    # gunzip gencode.v27.annotation.gff3.gz
    #
    ## buid the annotation database
    # python generate_gff3_db.py -i gencode.v27.annotation.gff3 -o gencode.v27.annotation.db -v    
    #
    # add featureset
    ga4gh_repo add-featureset ga4gh-example-data/registry.db read_and_variats_dataset <path to the annotation.db> -R GRCh37-lite -O so-xp

    # optional
    # add phenotype association set from Monarch Initiative
    # wget http://nif-crawler.neuinfo.org/monarch/ttl/cgd.ttl
    ga4gh_repo add-phenotypeassociationset ga4gh-example-data/registry.db read_and_variats_dataset <path to the folder containing cdg.ttl>

    # optional
    # add disease ontology set, like: NCIT
    # wget http://purl.obolibrary.org/obo/ncit.obo
    ga4gh_repo add-ontology -n NCIT ga4gh-example-data/registry.db ncit.obo

    # launch the server
    # at different IP and/or port: ga4gh_server --host 127.0.0.1 --port 8000
    ga4gh_server --host 127.0.0.1 --port 8000 -c NoAuth


    https://127.0.0.1:8000/


and then, from another terminal:

.. code:: bash

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' \
        http://127.0.0.1:8000/datasets/search \
        | jq '.'

giving:

.. code:: JSON

    {
      "datasets": [
        {
          "description": "PROFYLE test metadata",
          "id": "WyJQUk9GWUxFIl0",
          "name": "PROFYLE"
        }
      ]
    }
