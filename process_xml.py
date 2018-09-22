#!/usr/bin/env python3


from xml.etree import ElementTree
import collections
import os

Course = collections.namedtuple("Course", "title room building")


def main():
    folder = os.path.dirname(__file__)
    print("Folder == {}".format(folder))

    file = os.path.join(folder, "xml_data", "reed.xml")
    print("File == {}".format(file))

    with open(file) as fin:
        xml_text = fin.read()

    dom = ElementTree.fromstring(xml_text)
    # print(dom)

    # courses = dom.findall('course')
    course_nodes = dom.findall("course")

    courses = []
    for n in course_nodes:
        c = Course(
            n.find("title").text,
            n.find("place/room").text,
            n.find("place/building").text,
        )
        courses.append(c)

    building = input("What building are you in? ")
    room = input("What room are you in?")

    room_courses = [
        c.title for c in courses if c.building == building and c.room == room
    ]

    for c in room_courses:
        print("* " + c)


if __name__ == "__main__":
    main()
