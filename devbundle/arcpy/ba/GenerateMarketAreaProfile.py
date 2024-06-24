# Generated documentation for module arcpy.ba


class GenerateMarketAreaProfile(object):
    """
    Creates a segmentation profile by summarizing segments from standard geography boundaries within the input area.
    """

    @property
    def description(self) -> str:
        return """

        GenerateMarketAreaProfile_ba(in_features, segmentation_base, out_profile)

        Creates a segmentation profile by summarizing segments from standard
        geography boundaries within the input area.

     INPUTS:
      in_features (Feature Layer):
          The input feature class with polygon features used to create a
          segmentation area profile.
      segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset in use.

     OUTPUTS:
      out_profile (File):
          The name of the segmentation profile file to be created.

        """