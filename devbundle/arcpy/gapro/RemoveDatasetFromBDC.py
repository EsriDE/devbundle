# Generated documentation for module arcpy.gapro


class RemoveDatasetFromBDC(object):
    """
    Removes one or more datasets from an existing multifile feature connection (MFC). This tool only removes the dataset from the MFC file, the source data is not modified.
    """

    @property
    def description(self) -> str:
        return """

        RemoveDatasetFromBDC_gapro(bdc_datasets;bdc_datasets...)

        Removes one or more datasets from an existing multifile feature
        connection (MFC). This tool only removes the dataset from the MFC
        file, the source data is not modified.

     INPUTS:
      bdc_datasets (Table View):
          The datasets to remove from the .mfc file.

        """