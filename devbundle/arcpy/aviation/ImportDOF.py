# Generated documentation for module arcpy.aviation


class ImportDOF(object):
    """
    Adds, deletes, and updates the obstacle point features in an input obstacle feature class using an input digital obstacle file (DOF).
    """

    @property
    def description(self) -> str:
        return """

        ImportDOF_aviation(in_obstacle_file, obstacle_features)

        Adds, deletes, and updates the obstacle point features in an input
        obstacle feature class using an input digital obstacle file (DOF).

     INPUTS:
      in_obstacle_file (File):
          A DOF with a .DAT file extension. The contents of the DOF will be used
          to update the obstacle_features parameter values.
      obstacle_features (Feature Layer):
          The point feature class that will contain obstacle information from
          the DOF after execution.

        """