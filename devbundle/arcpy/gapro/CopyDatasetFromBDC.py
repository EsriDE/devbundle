# Generated documentation for module arcpy.gapro


class CopyDatasetFromBDC(object):
    """
    Copies a dataset from a multifile feature connection (MFC) to a feature class.
    """

    @property
    def description(self) -> str:
        return """

        CopyDatasetFromBDC_gapro(input_layer, output)

        Copies a dataset from a multifile feature connection (MFC) to a
        feature class.

     INPUTS:
      input_layer (Table View):
          The point, line, polygon, or table dataset that will be copied.

     OUTPUTS:
      output (Feature Class / Table):
          The output dataset that will be created when the MFC dataset is
          copied.

        """