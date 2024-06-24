# Generated documentation for module arcpy.management


class ExportAcknowledgementMessage(object):
    """
    Creates an output acknowledgement file to acknowledge the reception of previously received data change messages.
    """

    @property
    def description(self) -> str:
        return """

        ExportAcknowledgementMessage_management(in_geodatabase, out_acknowledgement_file, in_replica)

        Creates an output acknowledgement file to acknowledge the reception of
        previously received data change messages.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase from which to export the
          acknowledgement message. The geodatabase may be local or remote.
      in_replica (String):
          The replica from which the acknowledgement message will be exported.

     OUTPUTS:
      out_acknowledgement_file (File):
          Specifies the delta file to export to.

        """