import os
import sys
import argparse
from .render_template import render_template
from .get_images import get_images
from .copy_files import copy_files
from .get_assets import get_assets


def main():
    parser = argparse.ArgumentParser(
        description='Generate html album from images directory',
    )
    parser.add_argument('-i', action="store", default=".")
    parser.add_argument('-o', action="store", default="./output")
    parser.add_argument('-t', action="store")
    parser.add_argument('-d', action="store")

    # Parse arguments
    args = parser.parse_args()

    # Get source and destination directories
    source_dir = args.i
    dest_dir = args.o
    title = args.t
    description = args.d

    # Check if source destination exists
    if not os.path.isdir(source_dir):
        print("Error: source directory does not exists")
        sys.exit(1)

    # Check if destination directory exists
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    # Get image info from source
    images = get_images(source_dir)

    # Copy images to destination
    copy_files(images, dest_dir)

    # Copy assets to destination folder
    assets_path = "{}/assets".format(dest_dir)
    if not os.path.isdir(assets_path):
        os.makedirs(assets_path)
    assets = get_assets()
    copy_files(assets, assets_path)

    # Render template for images
    images_templates_list = []
    for img in images:
        img_rendering_dict = {
            "{{image-name}}": os.path.basename(img),
            "{{image-file}}": os.path.basename(img),
        }
        images_templates_list.append(render_template("image-template", img_rendering_dict))

    rendered_images = "".join(images_templates_list)

    # Render album template
    album_rendering_dict = {
        "{{title}}": title,
        "{{description}}": description,
        "{{image-placeholder}}": str(rendered_images),
    }
    album_template = render_template("album-template", album_rendering_dict)

    # Save rendered template in destination folder
    with open("{}/index.html".format(dest_dir), 'w') as f:
        f.write(album_template)

    # Output a nice message
    print("Done!")


if __name__ == '__main__':
    main()
