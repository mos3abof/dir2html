import os

from pkg_resources import resource_filename

def get_assets():
    assets = []

    assets_dirname = resource_filename(__name__, "resources/assets")
    for root, dirs, files in os.walk(assets_dirname):
        for file in files:
            try:
                full_path = '{}/{}'.format(os.path.realpath(root), file)
                assets.append(full_path)
            except IOError as e:
                print("Error: {}".format(e))

    return assets
