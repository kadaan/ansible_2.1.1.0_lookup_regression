import sys
import time

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def __init__(self, loader=None, templar=None, **kwargs):

        super(LookupModule, self).__init__(loader, templar, **kwargs)

        print("DEBUG: Lookup Initializing")

    def run(self, terms, variables, **kwargs):
        print("DEBUG: Lookup - {0}".format(terms[0]))
        time.sleep(1)
        return []
