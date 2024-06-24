# Generated documentation for module arcpy.indoors


class CreateIndoor3DDataset(object):
    """
    Creates an indoor 3D dataset containing the necessary multipatch feature classes to maintain floor plan data using a streamlined schema that conforms to the ArcGIS Indoors Information Model. You can use these feature classes when preparing 3D scenes of floor plans and share them across your organization.
    """

    @property
    def description(self) -> str:
        return """

        CreateIndoor3DDataset_indoors(target_gdb, indoor_dataset_name, spatial_reference)

        Creates an indoor 3D dataset containing the necessary multipatch
        feature classes to maintain floor plan data using a streamlined schema
        that conforms to the ArcGIS Indoors Information Model. You can use
        these feature classes when preparing 3D scenes of floor plans and
        share them across your organization.

     INPUTS:
      target_gdb (Workspace):
          The target file or enterprise geodatabase that will contain the indoor
          3D dataset.
      indoor_dataset_name (String):
          The unique name assigned to the output indoor dataset. The default is
          Indoor3D. If a dataset with this name exists in the target
          geodatabase, the indoor 3D feature classes will be created in that
          dataset.
      spatial_reference (Spatial Reference):
          The horizontal and vertical coordinate system of the output indoor 3D
          dataset.You can specify the spatial reference in several ways
          including the
          following:Reference a feature class or feature dataset with the
          spatial
          reference you want to apply, such as
          C:/workspace/myproject.gdb/indoors/details. Define a
          SpatialReference object. You can define the spatial
          reference object using either of the following:         Factory codes,
          for example: sr = arcpy.SpatialReference(3857,
          115700)Names, for example: sr = arcpy.SpatialReference("WGS 1984 Web
          Mercator
          (auxiliary sphere)", "WGS 1984")Use the well-known text (WKT) string
          of a spatial reference. One way
          to determine the WKT for a spatial reference is to export the spatial
          reference as a string, for example, arcpy.SpatialReference(3857,
          115700).exportToString().

        """