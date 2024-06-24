# Generated documentation for module arcpy.management


class ReExportUnacknowledgedMessages(object):
    """
    Creates an output delta file containing unacknowledged replica updates from a one-way or two-way replica geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ReExportUnacknowledgedMessages_management(in_geodatabase, output_delta_file, in_replica, in_export_option)

        Creates an output delta file containing unacknowledged replica updates
        from a one-way or two-way replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase from which the unacknowledged messages will be
          reexported. The geodatabase can be a local geodatabase or a geodata
          service.
      in_replica (String):
          The replica from which the unacknowledged messages will be reexported.
      in_export_option (String):
          Specifies the changes that will be reexported.ALL_UNACKNOWLEDGED-All
          changes with unacknowledged messages will be
          reexported.MOST_RECENT-Only those changes made since the last set of
          exported
          changes was sent will be reexported.

     OUTPUTS:
      output_delta_file (File):
          The delta file to which data changes will be reexported.

        """