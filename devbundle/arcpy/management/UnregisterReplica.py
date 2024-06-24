# Generated documentation for module arcpy.management


class UnregisterReplica(object):
    """
    Unregisters a replica from an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        UnregisterReplica_management(in_geodatabase, in_replica)

        Unregisters a replica from an enterprise geodatabase.

     INPUTS:
      in_geodatabase (Workspace):
          The enterprise geodatabase that contains the replica to unregister.
      in_replica (String):
          The name or ID of the replica that will be unregistered. If providing
          the replica name, it must be fully qualified, for example,
          myuser.myreplica.

        """