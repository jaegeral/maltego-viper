#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import viperhash
from common.viperapi import file_search_md5
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
    label='toSha256',
    description='returns a sha256 to a File',
    uuids=[ 'viper.tosha256' ],
    inputs=[ ( 'viper', viperhash ) ],
    debug=True
)
def dotransform(request, response, config):
    	progress(50)
	# Send a debugging message to the Maltego UI console
	#TODO: make it more flexible not only md5
	request_result=(file_search_md5(request.value))
	progress(60)
	debug(json.dumps(request_result, sort_keys=False, indent=5))
	for item in request_result:
		# create SHA256 Object
		sha256 = viperhash(item['sha256'])
    		sha256.hashtype = 'sha256'
		# Add entity to response object
		response += sha256
	progress(100)
	return response
