# Generated documentation for module arcpy.management


class CompareReplicaSchema(object):
    """
    Generates an .xml file that describes schema differences between a replica geodatabase and the relative replica geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CompareReplicaSchema_management(in_geodatabase, in_source_file, output_replica_schema_changes_file)

        Generates an .xml file that describes schema differences between a
        replica geodatabase and the relative replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase to which the replica schema will be compared.
          The geodatabase can be a local geodatabase or a geodata service.
      in_source_file (File):
          The file that contains the relative replica schema that will be used
          for the comparison.

     OUTPUTS:
      output_replica_schema_changes_file (File):
          The file that will contain a description of the schema differences.

        """