# Generated documentation for module arcpy.gapro


class PreviewDatasetFromBDC(object):
    """
    Creates a preview of the first ten features in a multifile feature connection (MFC) dataset.
    """

    @property
    def description(self) -> str:
        return """

        PreviewDatasetFromBDC_gapro(bdc_dataset, {out_preview_file})

        Creates a preview of the first ten features in a multifile feature
        connection (MFC) dataset.

     INPUTS:
      bdc_dataset (Table View):
          The dataset to preview from the MFC file.

     OUTPUTS:
      out_preview_file {File}:
          The output .csv file that represents a preview of your MFC dataset.

        """