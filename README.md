ficdl
=====

A script to download fanfiction from ffnet.

ficdl is a python script that takes a story url and downloads and converts it to a specified format.

Still in the initial stages.

* Uses calibre's ebook-convert for the conversion.
* Automatically creates table of contents

#### Usage:
```
    Usage: ./ficdl.py [option] [arg] [option] [arg]

    Options:
        -u <url>   Download story
        -f <file>  Use file to get list of urls.      
        -d <dir>   Save file to a specific destination.
        -t <type>  Specify one of three types mobi,epub or pdf for final save. Default is mobi.
```


To Do:
=====

* Use ebookmaker to convert, instead of depending on calibre.
* Add a licence
* Add a gui
* Convert hardcoded xpaths to python-readability
