# Generated documentation for module arcpy.conversion


class GPXtoFeatures(object):
    """
    Converts the point data in a .gpx file to features.
    """

    @property
    def description(self) -> str:
        return """

        GPXtoFeatures_conversion(Input_GPX_File, Output_Feature_class, Output_Type)

        Converts the point data in a .gpx file to features.

     INPUTS:
      Input_GPX_File (File):
          The input .gpx file to be converted.
      Output_Type (String):
          Specifies the geometry type of the output feature class.POINTS-An
          output point feature class will be created. All GPX points
          will be included in the output. This is the default.TRACKS_AS_LINES-An
          output polyline feature class will be created. Only
          GPX track points will be included in the output.

     OUTPUTS:
      Output_Feature_class (Feature Class):
          The output point feature class.

        """