#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import viperentity,viperhash
from common.viperapi import file_search
import json

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
    label='toName',
    description='returns Name for file',
    uuids=[ 'viper.toname' ],
    inputs=[ ( 'viper', viperhash ) ],
    debug=True
)
def dotransform(request, response, config):
    	progress(50)
	# Send a debugging message to the Maltego UI console
	#TODO: make it more flexible not only md5
	request_result=(file_search('md5',request.value))
	progress(60)
	debug(json.dumps(request_result, sort_keys=False, indent=5))
	for item in request_result:
		# create SHA256 Object
		e = viperentity(item['name'])
		# Add entity to response object
		response += e
	progress(100)
	return response


