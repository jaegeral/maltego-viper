#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'jaegeral'
__copyright__ = 'Copyright 2014, Viper Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'jaegeral'
__email__ = 'mail@alexanderjaeger.de'
__status__ = 'Development'

__all__ = [
    'viperentity',
    'viperhash',
    'vipertag',
    'vipername',
    'viperfile',
    'myViperEntity'
]

class viperentity(Entity):
    _namespace_ = 'viper'

@EntityField(name='hashtype', propname='hashtype', displayname='Hash Type')
class viperhash(viperentity):
    pass

#TODO: Remove
class MyViperEntity(viperentity):
    pass

class viperfile(viperentity):
    pass

class vipername(viperentity):
    pass

class vipertag(viperentity):
    pass



