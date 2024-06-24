# Generated documentation for module arcpy.topographic


class GeodatabaseToShape(object):
    """
    Exports one or more feature classes in a geodatabase to shapefiles using one of three modes: defense, generic, and Multinational Geospatial Co-Production Program (MGCP).
    """

    @property
    def description(self) -> str:
        return """

        GeodatabaseToShape_topographic(in_features;in_features..., output_folder, coded_value_domain_export_mode, conversion_method, create_empties)

        Exports one or more feature classes in a geodatabase to shapefiles
        using one of three modes: defense, generic, and Multinational
        Geospatial Co-Production Program (MGCP).

     INPUTS:
      in_features (Feature Layer):
          The features used to create the shapefiles.
      output_folder (Folder):
          The folder that will contain the output shapefiles.
      coded_value_domain_export_mode (String):
          Specifies the method that will be used to export coded domain
          values.DESCRIPTIONS-Coded domain values will be exported using their
          descriptions rather than raw values.VALUES-Coded domain values will be
          exported as raw values. This is the
          default.VALUES_AND_DESCRIPTIONS-Coded domain values will be exported
          as raw
          values and string descriptions
      conversion_method (String):
          Specifies the conversion method that will be
          applied.DEFENSE_BY_FEATURECLASS-A shapefile will be created based on
          the
          feature class name and trailing underscores will be removed from
          fields.DEFENSE_BY_SUBTYPE-A shapefile will be created based on the
          subtype
          name, attributes applicable to that subtype will be exported, and
          trailing underscores will be removed from fields. This is the
          default.GENERIC_BY_FEATURECLASS-A shapefile will be created for each
          feature
          class selected. The shapefile name must match the feature class
          name.GENERIC_BY_SUBTYPE-A shapefile will be created for each subtype
          of the
          feature class selected. The shapefile name must match the subtype
          name.MGCP-A shapefile will be created based on the feature class
          subtype.
          The exported shapefile will be named using the geometry type prefix,
          for example, S for surface features, L for line features, P for point
          features, and the feature code. For example, the river subtype BH140
          in the WatrcrsL feature class would be exported to a shapefile named
          LBH140.MUVD-A shapefile will be created based on the feature class
          subtype.
          The exported shapefile will be named using the geometry type prefix,
          for example, S for surface features, C for curve features, P for point
          features, and the feature code. For example, the river subtype BH140
          in the WatercrsL feature class would be exported to a shapefile named
          CBH140.
      create_empties (Boolean):
          Specifies whether empty shapefiles will be created if the input
          feature classes are empty.CREATE_EMPTIES-Empty shapefiles will be
          created if the corresponding
          input feature classes are empty.NO_CREATE_EMPTIES-Empty shapefiles
          will not be created if the
          corresponding input feature classes are empty. This is the default.

        """