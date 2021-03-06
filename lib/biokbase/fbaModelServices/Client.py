############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
# Passes on URLError, timeout, and BadStatusLine exceptions.
#     See: 
#     http://docs.python.org/2/library/urllib2.html
#     http://docs.python.org/2/library/httplib.html
#
############################################################

try:
    import json
except ImportError:
    import sys
    sys.path.append('simplejson-2.3.3')
    import simplejson as json
    
import urllib2, httplib
from urllib2 import URLError

class ServerError(Exception):

    def __init__(self, name, code, message):
        self.name = name
        self.code = code
        self.message = message

    def __str__(self):
        return self.name + ': ' + str(self.code) + '. ' + self.message

class fbaModelServices:

    def __init__(self, url, timeout = 30 * 60):
        if url != None:
            self.url = url
        self.timeout = int(timeout)
        if self.timeout < 1:
            raise ValueError('Timeout value must be at least 1 second')

    def get_models(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_models',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_fbas(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_fbas',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_gapfills(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_gapfills',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_gapgens(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_gapgens',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_reactions(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_reactions',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_compounds(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_compounds',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_media(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_media',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def get_biochemistry(self, input):

        arg_hash = { 'method': 'fbaModelServices.get_biochemistry',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def genome_object_to_workspace(self, input):

        arg_hash = { 'method': 'fbaModelServices.genome_object_to_workspace',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def genome_to_workspace(self, input):

        arg_hash = { 'method': 'fbaModelServices.genome_to_workspace',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def genome_to_fbamodel(self, input):

        arg_hash = { 'method': 'fbaModelServices.genome_to_fbamodel',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def export_fbamodel(self, input):

        arg_hash = { 'method': 'fbaModelServices.export_fbamodel',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def addmedia(self, input):

        arg_hash = { 'method': 'fbaModelServices.addmedia',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def export_media(self, input):

        arg_hash = { 'method': 'fbaModelServices.export_media',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def runfba(self, input):

        arg_hash = { 'method': 'fbaModelServices.runfba',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def export_fba(self, input):

        arg_hash = { 'method': 'fbaModelServices.export_fba',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def import_phenotypes(self, input):

        arg_hash = { 'method': 'fbaModelServices.import_phenotypes',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def simulate_phenotypes(self, input):

        arg_hash = { 'method': 'fbaModelServices.simulate_phenotypes',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def export_phenotypeSimulationSet(self, input):

        arg_hash = { 'method': 'fbaModelServices.export_phenotypeSimulationSet',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_runfba(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_runfba',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_gapfill_model(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_gapfill_model',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_gapgen_model(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_gapgen_model',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_wildtype_phenotype_reconciliation(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_wildtype_phenotype_reconciliation',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_reconciliation_sensitivity_analysis(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_reconciliation_sensitivity_analysis',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def queue_combine_wildtype_phenotype_reconciliation_params(self, input):

        arg_hash = { 'method': 'fbaModelServices.queue_combine_wildtype_phenotype_reconciliation_params',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def jobs_done(self, input):

        arg_hash = { 'method': 'fbaModelServices.jobs_done',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def check_job(self, input):

        arg_hash = { 'method': 'fbaModelServices.check_job',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')

    def run_job(self, input):

        arg_hash = { 'method': 'fbaModelServices.run_job',
                     'params': [input],
                     'version': '1.1'
                     }

        body = json.dumps(arg_hash)
        ret = urllib2.urlopen(self.url, body, timeout = self.timeout)
        if ret.code != httplib.OK:
            raise URLError('Received bad response code from server:' + ret.code)
        resp = json.loads(ret.read())

        if 'result' in resp:
            return resp['result'][0]
        elif 'error' in resp:
            raise ServerError(**resp['error'])
        else:
            raise ServerError('Unknown', 0, 'An unknown server error occurred')




        
