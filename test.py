#!/usr/bin/env python

import requests


def main():
    print('Hello World')
    r = requests.get('http://www.google.com')
    r.raise_for_status()
    print('Status:', r.status_code)


if __name__ == '__main__':
    main()
