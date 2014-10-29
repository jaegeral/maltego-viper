#!/usr/bin/env python

# Viper API python module for maltego transforms
# Author: Alexander Jaeger (@alexanderjaeger)

# Cuckoo API Documentation http://github.com/botherder/viper

import requests
from canari.config import config
from canari.maltego.utils import debug, progress
from canari.maltego.message import MaltegoException
import urllib2,urllib


import os
os.environ['no_proxy'] = '127.0.0.1,localhost,basf.net'


# Returns test result
def test(test):
    url = 'http://%s:%s/test' % (config['viper/host'], config['viper/port'])
    debug(url)
    try:
        r = requests.get(url)
	debug (r.json())
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)

#flexible API function
def file_search(key,value):
    url = 'http://%s:%s/file/find' % (config['viper/host'], config['viper/port'])
    debug(url)
    post_param = {key: value} 
    debug(post_param)
    try:
        r = requests.post(url,data=urllib.urlencode(post_param))
        debug (r.json())
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)


#flexible API function
def file_search(key,value):
    url = 'http://%s:%s/file/find' % (config['viper/host'], config['viper/port'])
    debug(url)
    post_param = {key: value} 
    debug(post_param)
    try:
        r = requests.post(url,data=urllib.urlencode(post_param))
        debug (r.json())
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)



def file_search_md5(md5):
    url = 'http://%s:%s/file/find' % (config['viper/host'], config['viper/port'])
    debug(url)
    post_param = {'md5': md5} 
    debug(post_param)
    try:
        r = requests.post(url,data=urllib.urlencode(post_param))
        debug (r.json())
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)


def file_search_tag(tag):
    url = 'http://%s:%s/file/find' % (config['viper/host'], config['viper/port'])
    debug(url)
    post_param = {'tag': tag} 
    debug(post_param)
    try:
        r = requests.post(url,data=urllib.urlencode(post_param))
        debug (r.json())
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)

# Returns file details from a sha256 hash
def file_search_sha256(sha256):
    url = 'http://%s:%s/file/find%s' % (config['viper/host'], config['viper/port'], sha256)
    try:
        r = requests.get(url)
        return r.json()
    except Exception as e:
        raise MaltegoException("The Transform has returned: %s" % e)


'''
# Submit file
#def submit_file(sample):
#    url = 'http://%s:%s/tasks/create/file' % (config['viper/host'], config['viper/port'])
#    samples = {'file': open(sample, 'rb')}
#    try:
#        r = requests.post(url, files=samples)
#        return r.json()
#    except Exception as e:
#        raise MaltegoException("The Transform has returned: %s" % e)
'''





