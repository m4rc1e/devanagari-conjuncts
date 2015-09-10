# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
from lxml import etree
import re
from collections import Counter

def main():
    xml_file = "./sourcedata/hiwiki-20150901-pages-meta-current.xml"
    count = Counter()
    devaConjuncts = ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"

    a = 0
    for event, element in etree.iterparse(xml_file):
        
        if 'text' in element.tag and element.text != None:
            texter = (element.text)
            conjuncts = re.findall(devaConjuncts, texter, re.UNICODE)
            for conjunct in conjuncts:
            	count[conjunct] += 1

    for i in sorted(count, key=count.get)[::-1]:
    	print(count[i], i.encode("utf-8"))


if __name__ == "__main__":
    main()