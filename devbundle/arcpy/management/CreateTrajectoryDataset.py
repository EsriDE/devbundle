# Generated documentation for module arcpy.management


class CreateTrajectoryDataset(object):
    """
    Creates an empty trajectory dataset in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateTrajectoryDataset_management(in_workspace, in_dataset_name, coordinate_system)

        Creates an empty trajectory dataset in a geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase where the trajectory dataset will be stored.
      in_dataset_name (String):
          The name of the trajectory dataset that will be created.
      coordinate_system (Coordinate System):
          The spatial reference of the trajectory dataset that will be created.

        """