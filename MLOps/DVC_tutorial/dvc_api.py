import dvc.api

with dvc.api.open(
    "get-started/data.xml",
    repo="https://github.com/iterative/dataset-registry"
) as fd:
    print("Opened")
    row = fd.readline()
    print(row)