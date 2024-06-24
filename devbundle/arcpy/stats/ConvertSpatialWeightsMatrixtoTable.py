# Generated documentation for module arcpy.stats


class ConvertSpatialWeightsMatrixtoTable(object):
    """
    Converts a binary spatial weights matrix file (.swm) to a table.
    """

    @property
    def description(self) -> str:
        return """

        ConvertSpatialWeightsMatrixtoTable_stats(Input_Spatial_Weights_Matrix_File, Output_Table)

        Converts a binary spatial weights matrix file (.swm) to a table.

     INPUTS:
      Input_Spatial_Weights_Matrix_File (File):
          The full pathname for the spatial weights matrix file (.swm) you want
          to convert.

     OUTPUTS:
      Output_Table (Table):
          A full pathname to the table you want to create.

        """