/*
A KBase module: eapearsonDemoGenomeEditClassification
*/

module eapearsonDemoGenomeEditClassification {
    typedef structure {
        string description;
    } ChangeLogEntry;

    typedef structure {
        /* Will be passed to viewer */
        string output_genome_ref;
        list<ChangeLogEntry> change_log;
        string title;

        /* To identify the viewer */
        string service_module_name;
        string widget_name;
    } UpdateGenomeClassificationMetadataResult;

    typedef structure {
        int workspace_id;
        string genome_ref;
        string output_genome_name; 
        string scientific_name;
    } UpdateGenomeClassificationMetadataParams;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef update_genome_classification_metadata(UpdateGenomeClassificationMetadataParams params) returns (UpdateGenomeClassificationMetadataResult output) authentication required;
};
