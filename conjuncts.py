# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from lxml import etree
import re
from collections import Counter
import unicodedata as uni

def human_name(conjunct):
    name = []
    for consonant in conjunct:
        if not "VIRAMA" in uni.name(unicode(consonant)):
            p = (uni.name(unicode(consonant)).split()[-1][:-1]).title()
            name.append(p)
    return 'd' + ''.join(name) + 'a'

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

    conjuncts_file = open("./conjuncts_Marathi_human_name.txt", "w")
    for conjunct in sorted(count, key=count.get)[::-1]:
    	conjuncts_file.write("%s %s %s\n" %(count[conjunct], conjunct.encode("utf-8"), human_name(conjunct)))
    conjuncts_file.close()
    print("Done!")


if __name__ == "__main__":
    main()