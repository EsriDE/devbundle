# Generated documentation for module arcpy.gapro


class DuplicateDatasetFromBDC(object):
    """
    Creates a duplicate of a multifile feature connection (MFC) dataset.
    """

    @property
    def description(self) -> str:
        return """

        DuplicateDatasetFromBDC_gapro(bdc_dataset, {duplicate_name})

        Creates a duplicate of a multifile feature connection (MFC) dataset.

     INPUTS:
      bdc_dataset (Table View):
          The MFC dataset to be duplicated.
      duplicate_name {String}:
          The name of the output MFC dataset.

        """