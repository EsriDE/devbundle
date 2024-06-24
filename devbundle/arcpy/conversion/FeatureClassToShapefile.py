# Generated documentation for module arcpy.conversion


class FeatureClassToShapefile(object):
    """
    Converts the features from one or more feature classes or feature layers to shapefiles and adds them to a folder of shapefiles.
    """

    @property
    def description(self) -> str:
        return """

        FeatureClassToShapefile_conversion(Input_Features;Input_Features..., Output_Folder)

        Converts the features from one or more feature classes or feature
        layers to shapefiles and adds them to a folder of shapefiles.

     INPUTS:
      Input_Features (Feature Layer):
          The list of input feature classes or feature layers that will be
          converted and added to the output folder.
      Output_Folder (Folder):
          The folder where the shapefiles will be written.

        """