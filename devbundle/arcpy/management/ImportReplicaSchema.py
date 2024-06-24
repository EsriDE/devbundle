# Generated documentation for module arcpy.management


class ImportReplicaSchema(object):
    """
    Applies replica schema differences using an input replica geodatabase and an XML schema file.
    """

    @property
    def description(self) -> str:
        return """

        ImportReplicaSchema_management(in_geodatabase, in_source)

        Applies replica schema differences using an input replica geodatabase
        and an XML schema file.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase to which the replica schema will be imported.
          The geodatabase can be a local geodatabase or a geodata service.
      in_source (File):
          The file that contains the replica schema differences that will be
          imported.

        """