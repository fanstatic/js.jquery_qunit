from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_qunit', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

css = ResourceInclusion(library, 'qunit.css')
qunit = ResourceInclusion(library, 'qunit.js', depends=[css, jquery])
