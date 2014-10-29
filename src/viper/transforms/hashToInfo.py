#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import Phrase
from common.entities import viperhash,vipername,vipertag
from common.viperapi import file_search_md5
import json


__author__ = 'jaegeral'
__copyright__ = 'Copyright 2014, Viper Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'jaegeral'
__email__ = 'mail@alexanderjaeger.de'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


#@superuser
@configure(
    label='md5 HashtoInfo',
    description='Returns Infos (all Hashes, vipertags)',
    uuids=[ 'viper.toAllInfo' ],
    inputs=[ ( 'viper', viperhash ) ],
    debug=True
)
def dotransform(request, response, config):
	# Report transform progress
	progress(50)
	# Send a debugging message to the Maltego UI console
	#TODO: make it more flexible not only md5
	request_result=(file_search_md5(request.value))
	progress(60)
	debug(json.dumps(request_result, sort_keys=False, indent=5))
	for item in request_result:
		for key in item.keys():
			for tag in item["tags"]:
				debug(tag)
				tag_obj = vipertag(tag)
				response += tag_obj
				
		## create MD5 object
		e = viperhash(item['md5'])
    		# Setting field values on the entity
    		e.hashtype = 'md5'
		debug(item)
		debug(item['name'])	
		# Add entity to response object
		response += e

		# create SHA256 Object
		sha256 = viperhash(item['sha256'])
    		sha256.hashtype = 'sha256'
		# Add entity to response object
		response += sha256

		# create SHA256 Object
		sha512 = viperhash(item['sha512'])
    		sha512.hashtype = 'sha512'
		# Add entity to response object
		response += sha512


		# Return response for visualization
	progress(100)
	return response


