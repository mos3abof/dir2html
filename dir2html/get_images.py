import os
import imghdr


def get_images(directory):
    images = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                full_path = '{}/{}'.format(os.path.realpath(root), file)

                img_type = imghdr.what(full_path)
                if img_type is not None:
                    images.append(full_path)
                # else:
                #     print("skipping [{}]...".format(full_path))
            except IOError as e:
                print("Error: {}".format(e))

    return images
