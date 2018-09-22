#!/usr/bin/env python3


from xml.etree import ElementTree
import os

def main():
    folder = os.path.basename(__file__)
    print('Folder == {}'.format(folder))

    file = os.path.join(folder, 'xml_data', 'reed.xml')
    print('File == {}'.format(file))


if __name__ == '__main__':
    main()
