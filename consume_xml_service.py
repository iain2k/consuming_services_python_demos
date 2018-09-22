#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from xml.etree import ElementTree
from dateutil.parser import parse
import collections

Episode = collections.namedtuple("Episode", "title link pubdate")


def get_xml_dom(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None

    dom = ElementTree.fromstring(resp.text)
    return dom


def get_episodes(dom):
    item_nodes = dom.findall("channel/item")
    print(len(item_nodes))

    episodes = [
        Episode(
            n.find("title").text, n.find("link").text, parse(n.find("pubDate").text)
        )
        for n in item_nodes
    ]

    return sorted(episodes, key=lambda e: e.pubdate)


def main():
    url = "https://talkpython.fm/rss"
    dom = get_xml_dom(url)
    print(dom)
    episodes = get_episodes(dom)
    print(episodes[:10])

    for idx, e in enumerate(episodes):
        print('{}. {}'.format(idx, e.title))


if __name__ == "__main__":
    main()
