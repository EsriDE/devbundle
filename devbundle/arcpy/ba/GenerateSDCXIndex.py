# Generated documentation for module arcpy.ba


class GenerateSDCXIndex(object):
    """
    Creates an index for a Statistical Data Collection (SDCX). The index will improve performance when using the custom data in analysis tools such as Enrich Layer.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSDCXIndex_ba(sdcx_file)

        Creates an index for a Statistical Data Collection (SDCX). The index
        will improve performance when using the custom data in analysis tools
        such as Enrich Layer.

     INPUTS:
      sdcx_file (File):
          The input Statistical Data Collection file (.sdcx).

        """