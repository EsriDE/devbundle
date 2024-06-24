# Generated documentation for module arcpy.indoors


class CreateIndoorNetworkDataset(object):
    """
    Creates an indoor network dataset containing the necessary feature classes to maintain indoor network data using a streamlined schema that conforms to the ArcGIS Indoors Information Model. The indoor network dataset can be used to support indoor routable networks.
    """

    @property
    def description(self) -> str:
        return """

        CreateIndoorNetworkDataset_indoors(target_gdb, indoor_network_dataset_name, spatial_reference)

        Creates an indoor network dataset containing the necessary feature
        classes to maintain indoor network data using a streamlined schema
        that conforms to the ArcGIS Indoors Information Model. The indoor
        network dataset can be used to support indoor routable networks.

     INPUTS:
      target_gdb (Workspace):
          The target file or enterprise geodatabase that will contain the output
          indoor network dataset.
      indoor_network_dataset_name (String):
          The unique name of the output indoor network dataset. This name is
          also used for the preliminary indoor network dataset. The default name
          for the indoor network dataset is IndoorNetwork. The default name for
          the preliminary indoor network dataset is PrelimIndoorNetwork.
      spatial_reference (Spatial Reference):
          The spatial reference of the output indoor network dataset.
          You can specify the spatial reference in several ways, including the
          following:        Reference a feature class or feature dataset with
          the spatial
          reference you want to apply, such as
          C:/workspace/myproject.gdb/indoors/details. Define a
          SpatialReference object. You can define the spatial
          reference object using either of the following:          Factory
          codes, for example: sr = arcpy.SpatialReference(3857,
          115700)Names, for example: sr = arcpy.SpatialReference("WGS 1984 Web
          Mercator
          (auxiliary sphere)", "WGS 1984")Use the well-known text (WKT) string
          of a spatial reference. One way
          to determine the WKT for a spatial reference is to export the spatial
          reference as a string, for example, arcpy.SpatialReference(3857,
          115700).exportToString().

        """