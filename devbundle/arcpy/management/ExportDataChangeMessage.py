# Generated documentation for module arcpy.management


class ExportDataChangeMessage(object):
    """
    Creates an output delta file containing updates from an input replica.
    """

    @property
    def description(self) -> str:
        return """

        ExportDataChangeMessage_management(in_geodatabase, out_data_changes_file, in_replica, switch_to_receiver, include_unacknowledged_changes, include_new_changes)

        Creates an output delta file containing updates from an input replica.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase from which the data change message will be
          exported. The geodatabase can be local or remote.
      in_replica (String):
          The replica containing the updates to be exported.
      switch_to_receiver (Boolean):
          Specifies whether the replica will be changed from a sender to a
          receiver. The receiver may not send replica updates until updates from
          the relative replica sender arrive.DO_NOT_SWITCH-The replica role will
          not be changed. This is the
          default.SWITCH-The replica role will be changed from a sender to
          receiver.
      include_unacknowledged_changes (Boolean):
          Specifies whether data changes that were previously exported for which
          no acknowledgment message was received will be
          included.NO_UNACKNOWLEDGED-Data changes that were previously sent will
          not be
          included.UNACKNOWLEDGED-All data changes that were previously exported
          for
          which no acknowledgment message was received will be included. This is
          the default.
      include_new_changes (Boolean):
          Specifies whether all data changes made since the last exported data
          change message will be included.NO_NEW_CHANGES-Data changes made since
          the last exported data change
          message will not be included.NEW_CHANGES-All data changes made since
          the last exported data change
          message will be included. This is the default.

     OUTPUTS:
      out_data_changes_file (File):
          The output delta file.

        """