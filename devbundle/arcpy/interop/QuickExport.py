# Generated documentation for module arcpy.interop


class QuickExport(object):
    """
    Converts one or more input feature classes or feature layers into any format supported by the ArcGIS Data Interoperability extension.
    """

    @property
    def description(self) -> str:
        return """

        QuickExport_interop(Input;Input..., Output)

        Converts one or more input feature classes or feature layers into any
        format supported by the ArcGIS Data Interoperability extension.

     INPUTS:
      Input (Feature Layer):
          The feature layers or feature classes that will be exported from ArcGIS

     OUTPUTS:
      Output (Interop Destination Dataset):
          The format and dataset to which the data will be exported.If the
          destination is a file with a well-known file extension, it can be
          given as-is. For instance, "c:\data\roads.gml".If the destination
          is not a file, or the file has an unknown extension, the format
          can be given as part of the argument, separated by a comma. For
          instance,"MIF,c:\data\". The names for supported formats can be
          found in the formats gallery, by opening up this tool in dialog
          mode and clicking the browse button.Additional format-specific
          parameters can be added after the dataset, separated by a comma.
          However, the syntax can be complex, so if this is required it is
          easiest to run the tool using its dialog  and copy the Python syntax
          from the Results window.

        """