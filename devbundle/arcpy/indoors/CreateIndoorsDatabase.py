# Generated documentation for module arcpy.indoors


class CreateIndoorsDatabase(object):
    """
    Creates an Indoors geodatabase that conforms to the ArcGIS Indoors Information Model and contains the feature classes, fields, and tables required for maintaining indoor data for floor plan mapping, routing, space planning, and workspace reservations.
    """

    @property
    def description(self) -> str:
        return """

        CreateIndoorsDatabase_indoors(target_gdb, {create_network}, {spatial_reference}, {create_attribute_rules})

        Creates an Indoors geodatabase that conforms to the ArcGIS Indoors
        Information Model and contains the feature classes, fields, and tables
        required for maintaining indoor data for floor plan mapping, routing,
        space planning, and workspace reservations.

     INPUTS:
      target_gdb (Workspace):
          The geodatabase that will contain the ArcGIS Indoors Information Model
          to manage indoor GIS information for use with Indoors apps.
      create_network {Boolean}:
          Specifies whether a network dataset containing the indoor
          transportation network feature classes-Landmarks, Pathways, and Floor
          Transitions-will be created in the Indoors database.CREATE_NETWORK-A
          network dataset and feature classes will be created.
          This is the default.NO_CREATE_NETWORK-A network dataset and feature
          classes will not be
          created.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output Indoors database. If no
          spatial reference is set, the output Indoors database will use WGS84
          Web Mercator (auxiliary sphere) as the horizontal coordinate system
          and WGS84 as the vertical coordinate system. You can specify the
          spatial reference in several ways, including the following:
          Reference a feature class or feature dataset with the spatial
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