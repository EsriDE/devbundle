# Generated documentation for module arcpy.management


class ExportTopologyErrors(object):
    """
    Exports the errors and exceptions from a geodatabase topology to the target geodatabase. All information associated with the errors and exceptions, such as the features referenced by the error or exception, is exported. Once the errors and exceptions are exported, the feature classes can be accessed using any license level of ArcGIS. The feature classes can be used with the Select Layer By Location tool and can be shared with other users who do not have access to the topology.
    """

    @property
    def description(self) -> str:
        return """

        ExportTopologyErrors_management(in_topology, out_path, out_basename)

        Exports the errors and exceptions from a geodatabase topology to the
        target geodatabase. All information associated with the errors and
        exceptions, such as the features referenced by the error or exception,
        is exported. Once the errors and exceptions are exported, the feature
        classes can be accessed using any license level of ArcGIS. The feature
        classes can be used with the Select Layer By Location tool and can be
        shared with other users who do not have access to the topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology from which the errors will be exported.
      out_path (Workspace / Feature Dataset):
          The output workspace in which the feature classes will be created.
      out_basename (String):
          The name to prefix to each output feature class. This allows you to
          specify unique output names when running multiple exports to the same
          workspace. The default is the topology name.

        """