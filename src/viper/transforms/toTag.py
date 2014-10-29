#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import viperhash,vipertag
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
    label='toTag',
    description='returns tag(s)',
    uuids=[ 'viper.totag' ],
    inputs=[ ( 'viper', viperhash ) ],
    debug=True
)
def dotransform(request, response, config):
    	# Report transform progress
	progress(50)
	# Send a debugging message to the Maltego UI console
	#TODO: make it more flexible not only md5
	request_result=(file_search('md5',request.value))
	progress(60)
	debug(json.dumps(request_result, sort_keys=False, indent=5))
	for item in request_result:
		for key in item.keys():
			for tag in item["tags"]:
				debug(tag)
				tag_obj = vipertag(tag)
				response += tag_obj
	progress(100)
	return response
