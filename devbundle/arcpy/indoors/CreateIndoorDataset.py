# Generated documentation for module arcpy.indoors


class CreateIndoorDataset(object):
    """
    Creates an indoor dataset containing the necessary feature classes to maintain floor plan data using a streamlined schema that conforms to the ArcGIS Indoors Information Model.
    """

    @property
    def description(self) -> str:
        return """

        CreateIndoorDataset_indoors(target_gdb, indoor_dataset_name, spatial_reference, {create_attribute_rules})

        Creates an indoor dataset containing the necessary feature classes to
        maintain floor plan data using a streamlined schema that conforms to
        the ArcGIS Indoors Information Model.

     INPUTS:
      target_gdb (Workspace):
          The target file or enterprise geodatabase that will contain the output
          indoor dataset.
      indoor_dataset_name (String):
          The unique name of the output indoor dataset. The default is Indoor.
      spatial_reference (Spatial Reference):
          The horizontal and vertical coordinate system of the output
          indoor dataset. You can specify the spatial reference in several ways,
          including the following:        Reference a feature class or feature
          dataset with the spatial
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
      create_attribute_rules {Boolean}:
          Specifies whether attribute rules and the associated fields and error
          datasets will be created in the Indoors database. These attribute
          rules include validation checks to use in quality control workflows
          for floor plan data. The target geodatabase must be a file geodatabase
          or an enterprise geodatabase configured for branch
          versioning.CREATE_RULES-Attribute rules and error layers will be
          created. This
          is the default.NO_CREATE_RULES-Attribute rules and error layers will
          not be created.

        """