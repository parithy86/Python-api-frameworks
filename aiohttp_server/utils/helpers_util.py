import yaml


def read_yaml_configs(file):
    with open(file) as file:
        data = yaml.full_load(file)

    return data
