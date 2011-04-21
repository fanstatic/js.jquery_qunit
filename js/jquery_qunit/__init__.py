from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_qunit', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

css = Resource(library, 'qunit.css')
qunit = Resource(library, 'qunit.js', depends=[css, jquery])
