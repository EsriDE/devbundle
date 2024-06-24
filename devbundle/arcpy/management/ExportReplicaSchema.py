# Generated documentation for module arcpy.management


class ExportReplicaSchema(object):
    """
    Creates a replica schema file with the schema of an input one- or two- way replica.
    """

    @property
    def description(self) -> str:
        return """

        ExportReplicaSchema_management(in_geodatabase, output_replica_schema_file, in_replica)

        Creates a replica schema file with the schema of an input one- or two-
        way replica.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase from which the replica schema will be
          exported. The geodatabase can be a local or remote geodatabase.
      in_replica (String):
          The replica from which the schema will be exported.

     OUTPUTS:
      output_replica_schema_file (File):
          The file to which the replica schema will be exported.

        """