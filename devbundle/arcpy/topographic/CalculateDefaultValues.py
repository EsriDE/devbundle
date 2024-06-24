# Generated documentation for module arcpy.topographic


class CalculateDefaultValues(object):
    """
    Replaces null values in a feature class or table with the default values from the geodatabase feature class.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDefaultValues_topographic(in_datasets;in_datasets...)

        Replaces null values in a feature class or table with the default
        values from the geodatabase feature class.

     INPUTS:
      in_datasets (Table View / Feature Layer / Dataset):
          The feature classes and/or tables whose null values will be replaced
          with the default values from the data model.

        """