# Generated documentation for module arcpy.intelligence


class DOFToObstacleFeatures(object):
    """
    Converts the U.S. Federal Aviation Administration (FAA) Digital Obstacle File (DOF) to obstruction points and obstruction buffer features.
    """

    @property
    def description(self) -> str:
        return """

        DOFToObstacleFeatures_intelligence(in_table, out_obstacle_features, out_obstacle_buffers, {clip_features})

        Converts the U.S. Federal Aviation Administration (FAA) Digital
        Obstacle File (DOF) to obstruction points and obstruction buffer
        features.

     INPUTS:
      in_table (Table View):
          The input DOF table to convert into obstacle features.
      clip_features {Feature Layer}:
          An area to clip from the in_table. Only obstacles within this area
          will be created and buffered.

     OUTPUTS:
      out_obstacle_features (Feature Class):
          The point obstacle features created from the in_table.
      out_obstacle_buffers (Feature Class):
          The distance buffers created at 10 times the value of thefield
          in the in_table. AGL

        """