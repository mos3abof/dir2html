import os


def get_assets():
    assets = []

    for root, dirs, files in os.walk("dir2html/resources/assets"):
        for file in files:
            try:
                full_path = '{}/{}'.format(os.path.realpath(root), file)
                assets.append(full_path)
                # else:
                #     print("skipping [{}]...".format(full_path))
            except IOError as e:
                print("Error: {}".format(e))

    return assets
