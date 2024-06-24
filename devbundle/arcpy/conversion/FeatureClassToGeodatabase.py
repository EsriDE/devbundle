# Generated documentation for module arcpy.conversion


class FeatureClassToGeodatabase(object):
    """
    Converts one or more feature classes or feature layers to geodatabase feature classes.
    """

    @property
    def description(self) -> str:
        return """

        FeatureClassToGeodatabase_conversion(Input_Features;Input_Features..., Output_Geodatabase)

        Converts one or more feature classes or feature layers to geodatabase
        feature classes.

     INPUTS:
      Input_Features (Feature Layer):
          One or more feature classes or feature layers that will be imported
          into a geodatabase.
      Output_Geodatabase (Workspace / Feature Dataset):
          The output or destination geodatabase.

        """