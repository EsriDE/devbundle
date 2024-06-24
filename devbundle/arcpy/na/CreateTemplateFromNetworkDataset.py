# Generated documentation for module arcpy.na


class CreateTemplateFromNetworkDataset(object):
    """
    Creates a file containing the schema of an existing network dataset. This template file can then be used to create a new network dataset with the same schema.
    """

    @property
    def description(self) -> str:
        return """

        CreateTemplateFromNetworkDataset_na(network_dataset, output_network_dataset_template)

        Creates a file containing the schema of an existing network dataset.
        This template file can then be used to create a new network dataset
        with the same schema.

     INPUTS:
      network_dataset (Network Dataset Layer):
          The network dataset whose schema will be written to the output
          template file.

     OUTPUTS:
      output_network_dataset_template (File):
          The output file (.xml) that will contain the schema of the input
          network dataset.

        """