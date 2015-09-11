Apache Libcloud - Modification for Interoute VDC
================================================

Modification of Apache Libcloud <http://libcloud.apache.org> for use of the 'cloudstack' provider code with 
Interoute Virtual Data Centre, which requires an additional parameter for the VDC regions.

Modified file: libcloud/common/cloudstack.py

How to install
--------------

[to do]


How to use
----------

Set the following environment variable before running libcloud commands in Python: 

    export CLOUDSTACK_VDC_REGION='Asia'
    python region_environment_test.py



