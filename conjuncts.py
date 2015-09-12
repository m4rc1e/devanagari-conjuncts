# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from lxml import etree
import re
from collections import Counter

def main():
    corpus_folder = "./sourcedata/"

    count = Counter()
    devaConjuncts = ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"

    for xml in os.listdir(corpus_folder):
        if not xml.startswith('.'):
            print("Parsing %s" %xml)
            for event, element in etree.iterparse(corpus_folder+xml):
                if 'text' in element.tag and element.text != None:
                    texter = (element.text)
                    conjuncts = re.findall(devaConjuncts, texter, re.UNICODE)
                    for conjunct in conjuncts:
                    	count[conjunct] += 1

    conjuncts_file = open("./conjuncts_all.txt", "w")
    for conjunct in sorted(count, key=count.get)[::-1]:
    	conjuncts_file.write("%s %s\n" %(count[conjunct], conjunct.encode("utf-8")))
    conjuncts_file.close()
    print("Done!")


if __name__ == "__main__":
    main()