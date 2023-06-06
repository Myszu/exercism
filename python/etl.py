def transform(legacy_data):
    output = {}
    for key in legacy_data.keys():
        for item in legacy_data.get(key):
            output[str(item).lower()] = key
    return output
