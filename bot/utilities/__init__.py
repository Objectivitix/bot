def get_yaml_val(yaml_file: str, *strings: str) -> dict:
    from string import punctuation

    import yaml

    return_dict = {}

    for string in strings:
        sep_string = "".join(
            [" " if char in punctuation else char for char in string]
        ).split()

        with open(yaml_file, encoding="utf-8") as config:

            data = yaml.load(config, Loader=yaml.UnsafeLoader)

            for key in sep_string:

                if key in data:
                    data = data[key]

                    if key == sep_string[-1]:
                        return_dict[key] = data

                else:
                    raise yaml.YAMLError(f'Key "{key}" cannot be found')

    return return_dict
