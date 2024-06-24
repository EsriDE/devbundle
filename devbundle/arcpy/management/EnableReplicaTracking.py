# Generated documentation for module arcpy.management


class EnableReplicaTracking(object):
    """
    Enables replica tracking on data, allowing you to work with offline maps and in distributed collaborations. Replica tracking applies to services that are configured with the sync capability with the option of creating a version for each downloaded map.
    """

    @property
    def description(self) -> str:
        return """

        EnableReplicaTracking_management(in_dataset)

        Enables replica tracking on data, allowing you to work with offline
        maps and in distributed collaborations. Replica tracking applies to
        services that are configured with the sync capability with the option
        of creating a version for each downloaded map.

     INPUTS:
      in_dataset (Table / Feature Class / Feature Dataset):
          The enterprise geodatabase table, feature class, feature dataset,
          attributed relationship class, or many-to-many relationship class on
          which to enable replica tracking.

        """