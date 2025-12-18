# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "daft[unity]>=0.6.14",
# ]
# ///

import os
import sys

import daft
from daft.catalog import Catalog
from daft.unity_catalog import UnityCatalog


def set_catalog():
    endpoint = os.environ.get("db_endpoint")
    apikey = os.environ.get("db_api_key")
    if endpoint is None or apikey is None:
        return
    unity_catalog = UnityCatalog(endpoint=endpoint, token=apikey)
    catalog = daft.Catalog.from_unity(unity_catalog)
    daft.attach_catalog(catalog, "my_unity_catalog")
    print("catalog:", catalog)


def main():
    print("Hello from unity!")
    print("\nenv:", os.environ)
    set_catalog()
    for c in daft.list_catalogs():
        print("catalog:", c)
    # catalog = daft.get_catalog("my_unity_catalog")
    # print("\ncatalog:", catalog)


def run(catalog: Catalog):
    print("running unity catalog!")
    print(sys.version)
    print("daft version", daft.__version__)
    print(catalog)
    print("tables:", catalog.list_tables())
    # table = catalog.get_table("jaytest-unity.daft_test.source_data")
    table = catalog.get_table("jaytest-unity.demo.reddit_irl_images_index")

    # Read the table as a DataFrame
    table.read()
    df = table.read(ignore_deletion_vectors=True)
    df_limited = df.limit(10)
    df_limited.show()


if __name__ == "__main__":
    main()
