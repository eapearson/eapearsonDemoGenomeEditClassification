# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport

#END_HEADER


class eapearsonDemoGenomeEditClassification:
    '''
    Module Name:
    eapearsonDemoGenomeEditClassification

    Module Description:
    A KBase module: eapearsonDemoGenomeEditClassification
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def update_genome_classification_metadata(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type
           "UpdateGenomeClassificationMetadataParams" -> structure: parameter
           "workspace_id" of Long, parameter "genome_ref" of String,
           parameter "output_genome_name" of String, parameter
           "scientific_name" of String
        :returns: instance of type "UpdateGenomeClassificationMetadataResult"
           -> structure: parameter "output_genome_ref" of String, parameter
           "change_log" of list of type "ChangeLogEntry" -> structure:
           parameter "description" of String, parameter "service_module_name"
           of String, parameter "widget_name" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN update_genome_classification_metadata
        # Fake it for now...

        output = {
            "output_genome_ref": params["genome_ref"],
            "change_log": ["foo", "bar", "baz"]
        }
        #END update_genome_classification_metadata

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method update_genome_classification_metadata return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
