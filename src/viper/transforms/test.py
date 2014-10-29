#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.viperapi import test
from common.entities import viperhash,vipertag

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


"""
TODO: set the appropriate configuration parameters for your transform.
TODO: Uncomment the line below if the transform needs to run as super-user
"""
#@superuser
@configure(
    label='this will test your Viper instance API',
    description='Returns /test result',
    uuids=[ 'viper.test' ],
    inputs=[ ( 'viper', viperhash ),( 'viper', vipertag )],
    debug=True
)
def dotransform(request, response, config):
	debug(test('foo'))  
	return response

