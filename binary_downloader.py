#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from xml.etree import ElementTree
import os
import shutil


def get_episode_files(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    xml_text = resp.text
    dom = ElementTree.fromstring(xml_text)

    return [
        enclosure_node.attrib["url"]
        for enclosure_node in dom.findall("channel/item/enclosure")
    ]


def download_file(file, dest_folder):

    resp = requests.get(file, stream=True)
    if resp.status_code != 200:
        return None

    resp.decode_content = True

    dest_folder = os.path.expanduser(dest_folder)
    if not os.path.exists(dest_folder):
        print('making destination folder', dest_folder)
        os.makedirs(dest_folder)
    else:
        print('Directory {} already exists'.format(dest_folder))

    base_file = os.path.basename(file)
    dest_file = os.path.join(
        dest_folder,
        base_file)
    print('DEST_FOLDER', dest_folder)
    print('BASE FILE', base_file)
    print('DEST_FILE', dest_file)
    print()

    with open(dest_file, 'wb') as fileout:
        shutil.copyfileobj(resp.raw, fileout)


def main():
    mp3_files = get_episode_files("https://talkpython.fm/rss")
    for file in mp3_files[:3]:
        print(file)
        download_file(file, "~/Desktop/mp3s/")


if __name__ == "__main__":
    main()
