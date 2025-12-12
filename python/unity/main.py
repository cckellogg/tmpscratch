import os

import daft
from daft.unity_catalog import UnityCatalog


def set_catalog():
    endpoint = os.environ.get("db_endpoint")
    apikey = os.environ.get("db_api_key")
    if endpoint is None or apikey is None:
        return
    unity_catalog = UnityCatalog(endpoint=endpoint, token=apikey)
    catalog = daft.Catalog.from_unity(unity_catalog)
    daft.attach_catalog(catalog, "my_unity_catalog")


def main():
    print("Hello from unity!")
    print("\nenv:", os.environ)
    set_catalog()
    catalog = daft.get_catalog("my_unity_catalog")
    print("\ncatalog:", catalog)


if __name__ == "__main__":
    main()
