Apache Libcloud - Modification for Interoute VDC
================================================

Version: 2015-09-12

Modification of Apache Libcloud <http://libcloud.apache.org> for use  with 
Interoute Virtual Data Centre, which requires an additional parameter 'region' for the VDC regions.

SIMPLE FIRST VERSION
--------------------

Modified the provider CLOUDSTACK file 'libcloud/common/cloudstack.py' to read the region parameter from an environment variable 'CLOUDSTACK_VDC_REGION'.

How to install
--------------

   $ sudo pip install backports.ssl_match_hostname  # MAY BE REQUIRED

   $ sudo pip install git+https://github.com/Interoute/libcloud.git@interoute_mod_region#egg=apache-libcloud


How to use
----------

Set the following environment variable before running libcloud commands in Python: 

   $ export CLOUDSTACK_VDC_REGION='Asia'

Valid values are 'Europe', 'USA', or 'Asia', and the case is not significant. Default value is 'Europe' if no environment variable is set. 

As a quick test, the following program will output the VDC zones, which should be those located in the specified region::

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security
# For secure http, set to server without certificate
libcloud.security.VERIFY_SSL_CERT = True
Driver = get_driver(Provider.CLOUDSTACK)
api_secret = "INSERT VDC API SECRET KEY"
api_key = "INSERT VDC API KEY"
vdchost =  "INSERT VDC API SERVER ADDRESS"
vdcpath = "INSERT PATH TO THE API ENDPOINT"
conn=Driver(key=api_key, secret=api_secret, host=vdchost, path=vdcpath)
# As a test, print the list of VDC zones for the specified region
print conn.list_locations()




