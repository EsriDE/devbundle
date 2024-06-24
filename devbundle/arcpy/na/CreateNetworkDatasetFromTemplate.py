# Generated documentation for module arcpy.na


class CreateNetworkDatasetFromTemplate(object):
    """
    Creates a new network dataset with the schema contained in the input template file (.xml). All the feature classes and input tables required for creating the network dataset must already exist before this tool is executed.
    """

    @property
    def description(self) -> str:
        return """

        CreateNetworkDatasetFromTemplate_na(network_dataset_template, output_feature_dataset)

        Creates a new network dataset with the schema contained in the input
        template file (.xml). All the feature classes and input tables
        required for creating the network dataset must already exist before
        this tool is executed.

     INPUTS:
      network_dataset_template (File):
          The template file (.xml) created by the Create Template From Network
          Dataset tool containing the schema of the output network dataset to be
          created.
      output_feature_dataset (Feature Dataset):
          The feature dataset containing the feature classes that will take part
          in the network dataset being created. The network will be created in
          this dataset using the name specified in the network dataset template.

        """