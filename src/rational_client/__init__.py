import os
import sys
# Add the vendor directory to the system path
vendor_dir = os.path.join(os.path.dirname(__file__), '_vendor')
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)


import os
import sys

# Add the vendor directory to the system path to allow local imports
vendor_dir = os.path.join(os.path.dirname(__file__), '_vendor')
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)
