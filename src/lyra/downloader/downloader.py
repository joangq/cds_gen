from lyra.auth import Client

name_mapping = dict(
    area_group = 'area',
    data_format = 'format'
)

def collapse_names(d: dict, names, queue):
    if len(queue) == 0:
        return d
    
    name = queue.pop(0)

    if not name in d or not name in names:
        return collapse_names(d, names, queue)

    d[names[name]] = d[name]
    del d[name]
    return collapse_names(d, names, queue)

def process_download_data(collection_name: str, parameters: dict):
    parameters = collapse_names(parameters, name_mapping, list(parameters.keys()))

    print(collection_name, parameters)

    Client().retrieve(
        collection_name,
        parameters,
        'data'
    )

def download_data(**kwargs):
    collection_name = kwargs.pop('collection_name')
    return process_download_data(collection_name, kwargs)