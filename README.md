HL7apy is a lightweight Python package to intuitively handle [HL7](http://www.hl7.org) v2 messages according to HL7 specifications.

The main features includes:

 * Message parsing
 * Message creation
 * Message validation following the HL7 xsd specifications
 * Access to elements by name, long name or position
 * Support to all simple and complex datatypes
 * Encoding chars customization
 * Message encoding in ER7 format and compliant with MLLP protocol
 * Support to message profile
 * Support to Z-Elements
 * Simple MLLP server implementation

Currently supported HL7 versions are: 2.1, 2.2, 2.3, 2.3.1, 2.4, 2.5, 2.5.1, 2.6, 2.7, 2.8, 2.8.1, 2.8.2

Current version is __1.3.4__

This project is not affiliated with the HL7 organization: the library is just consistent with their specification.

Documentation can be found [here](http://crs4.github.io/hl7apy/).

Installation
------------

HL7apy is platform independent and supports Python 2.7 and Python 3.4, 3.5, 3.6, 3.7

To install it get the latest release from [GitHub](https://github.com/crs4/hl7apy/releases) and launch the following command:

```bash
  python setup.py install
```

Alternatively you can use pip to install it from [PyPI](https://pypi.python.org/pypi/hl7apy/)

```bash
  pip install hl7apy
```

[![Build Status](https://travis-ci.org/crs4/hl7apy.png)](https://travis-ci.org/crs4/hl7apy)

[![Code Health](https://landscape.io/github/crs4/hl7apy/develop/landscape.svg?style=flat)](https://landscape.io/github/crs4/hl7apy/develop)

[![Coverage Status](https://coveralls.io/repos/crs4/hl7apy/badge.svg)](https://coveralls.io/r/crs4/hl7apy)

External Links
--------------

Michael Sarfati wrote an interesting 2-parts article on his blog about HL7apy with useful examples and tutorials. 
You can read it [here](https://msarfati.wordpress.com/2015/06/20/python-hl7-v2-x-and-hl7apy-introduction-and-parsing-part-1/). 
Thanks a lot Michael for your contribution.


License
-------

HL7apy is released under the MIT License.

Copyright (c) 2012-2018, CRS4

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

