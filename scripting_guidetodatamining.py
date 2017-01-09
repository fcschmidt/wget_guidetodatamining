#!/usr/bin/env python
"""
    My Simple scripting used to download pdf's
    http://guidetodatamining.com
"""
import urllib.request
import os.path
import errno
import time


ch = 1
while ch <= 8:
    url = 'http://guidetodatamining.com/assets/guideChapters/DataMining-ch{0}.pdf'.format(ch)
    open_link = urllib.request.urlopen(url)
    filename = url[-18:]

    pathname = os.path.expanduser('~/Downloads/GuidetoDataMining/')
    if not os.path.exists(pathname):
        try:
            os.makedirs(pathname)
            print("Directory created successfully!")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    print("Accessing %s " % url)

    time.sleep(2)
    print("Starting download...")

    with open(pathname+filename, 'wb') as f:
        f.write(open_link.read())
    print("Download complete!")
    ch += 1
