#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.config import config
from common.entities import viperhash
from common.entities import vipertag
from common.viperapi import file_search_tag
import json

import json 
import urllib
import urllib2
import requests

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

#@superuser
@configure(
    label='tagToHash(finds files to tag)',
    description='Resturns a hash (or a list of) for a given Tag',
    uuids=[ 'viper.tagToHash' ],
    inputs=[ ( 'viper', vipertag ) ],
    debug=True
)
def dotransform(request, response, config):
    	# Report transform progress
	progress(50)
	# Send a debugging message to the Maltego UI console
	#TODO: make it more flexible not only md5
	request_result=(file_search_tag(request.value))
	progress(60)
	debug(json.dumps(request_result, sort_keys=False, indent=5))
	for item in request_result:				
		## create MD5 object
		e = viperhash(item['md5'])
    		# Setting field values on the entity
    		e.hashtype = 'md5'
		#debug(item)
		#debug(item['name'])	
		# Add entity to response object
		response += e
		# Return response for visualization
	progress(100)
	return response
