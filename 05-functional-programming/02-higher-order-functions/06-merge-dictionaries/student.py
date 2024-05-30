def merge_dictionaries(d1, d2, merge_function):
    merged_dict = dict(d1)
    for k, v in d2.items():
        if k in merged_dict.keys():
            merged_dict[k] = merge_function(merged_dict[k], v)

        else:
            merged_dict[k] = v

    return merged_dict
