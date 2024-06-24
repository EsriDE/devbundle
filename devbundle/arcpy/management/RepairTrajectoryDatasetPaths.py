# Generated documentation for module arcpy.management


class RepairTrajectoryDatasetPaths(object):
    """
    Repairs paths to source data for a trajectory dataset.
    """

    @property
    def description(self) -> str:
        return """

        RepairTrajectoryDatasetPaths_management(in_trajectory_dataset, paths_list;paths_list..., {where_clause})

        Repairs paths to source data for a trajectory dataset.

     INPUTS:
      in_trajectory_dataset (Trajectory Layer):
          The input trajectory dataset.
      paths_list (Value Table):
          A list of paths to remap.
      where_clause {SQL Expression}:
          An SQL expression that will limit the repairs to selected items in the
          trajectory dataset.

        """