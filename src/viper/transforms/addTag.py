#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import viperentity,viperhash
from common.viperapi import file_search
__author__ = 'jaegeral'
__copyright__ = 'Copyright 2014, Viper Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'jaegeral'
__email__ = 'mail@alexanderjaeger.de'
__status__ = 'Development'

__all__ = [
    'dotransform'
]



@configure(
    label='addTag',
    description='adds a tag to a hash',
    uuids=[ 'viper.addTag' ],
    inputs=[ ( 'viper', viperhash ) ],
    debug=True
)
def dotransform(request, response, config):
    	msg = 'Enter Search Criteria'
	title = 'L0 - Simple pcap search [SmP]'
	fieldNames = ["Source", "Destination", "Port", "Free Text"]
	fieldValues = []
	fieldValues = multenterbox(msg, title, fieldNames)

	#This shows a box with 4 parameter fields which you then reference in your transform like this:

	#s_ip = fieldValues[0]
    	return response


