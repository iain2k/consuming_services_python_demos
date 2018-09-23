#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from xml.etree import ElementTree
import os


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

    base_file = os.path.basename(file)
    dest_file = os.path.join(
        os.path.abspath(dest_folder),
        base_file)

    print('BASE FILE', base_file)
    print('DEST_FILE', dest_file)

    # dest_file = open()


def main():
    mp3_files = get_episode_files("https://talkpython.fm/rss")
    for file in mp3_files[:3]:
        print(file)
        download_file(file, "~/Desktop/mp3s/")


if __name__ == "__main__":
    main()
