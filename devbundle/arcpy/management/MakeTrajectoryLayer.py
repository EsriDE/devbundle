# Generated documentation for module arcpy.management


class MakeTrajectoryLayer(object):
    """
    Generates a feature layer from selected variables in a trajectory file.
    """

    @property
    def description(self) -> str:
        return """

        MakeTrajectoryLayer_management(in_trajectory_file, out_trajectory_layer, {dimension}, {predefined_variables;predefined_variables...}, {variables;variables...})

        Generates a feature layer from selected variables in a trajectory
        file.

     INPUTS:
      in_trajectory_file (Raster Dataset / Trajectory Layer):
          The input trajectory file.
      dimension {String}:
          The dimension name. The first dimension is used by default.
      predefined_variables {String}:
          Specifies the predefined variables that will be used for measurement
          for different sensor types.SIGMA0-A variable that contains Surface
          Backscatter Coefficient will
          be used.SSH-A variable that contains Sea Surface Height will be
          used.SSHA-A variable that contains Sea Surface Height Anomaly will be
          used.SWH-A variable that contains Significant Wave Height will be
          used.SIGMA0_OCEAN-A variable that contains Ocean Surface Backscatter
          Coefficient will be used.H_SEA_ICE-A variable that contains Sea Ice
          Surface Elevation will be
          used.H_SEA_ICE_ANOMALY-A variable that contains Sea Ice Surface Height
          Anomaly will be used.SIC-A variable that contains Sea Ice
          Concentration will be used.SIGMA0_SEA_ICE-A variable that contains Sea
          Ice Surface Backscatter
          Coefficient will be used.H_ICE_SHEET-A variable that contains Ice
          Sheet Surface Elevation will
          be used.SIGMA0_ICE_SHEET-A variable that contains Ice Sheet Surface
          Backscatter Coefficient will be used.H_ICE-A variable that contains
          Ice Surface Elevation will be used.SIGMA0_ICE-A variable that contains
          Ice Surface Backscatter
          Coefficient will be used.WS-A variable that contains Wind Speed will
          be used.H_MSS-A variable that contains Mean Sea Surface Elevation will
          be
          used.
      variables {String}:
          The variables that will be included in the output layer. All variables
          are selected by default.

     OUTPUTS:
      out_trajectory_layer (Trajectory Layer):
          The output feature layer that contains the selected variables.

        """