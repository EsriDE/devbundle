# Generated documentation for module arcpy.maritime


class GenerateLandAreas(object):
    """
    Creates land area polygon features by identifying existing land topology features, such as coastline and shoreline construction, and eliminating any polygons over water or other exclusionary features. An area of interest is specified to limit the processing area.
    """

    @property
    def description(self) -> str:
        return """

        GenerateLandAreas_maritime(in_workspace, target_workspace, in_extent_polygon, {in_configuration_file})

        Creates land area polygon features by identifying existing land
        topology features, such as coastline and shoreline construction, and
        eliminating any polygons over water or other exclusionary features. An
        area of interest is specified to limit the processing area.

     INPUTS:
      in_workspace (Workspace):
          The workspace containing a Maritime product schema (S-57 or S-101
          based) in which existing land topology features, such as coastline and
          shoreline construction, will be processed to identify the land areas
          that will be created.
      target_workspace (Workspace):
          The workspace that will contain the land area polygons that are
          created. The workspace must be a Nautical workspace with S-57 or S-101
          schema. For S-57 schema, the workspace should have a NaturalFeaturesA
          polygon feature class with a LNDARE_LandArea subtype. For S-101
          schema, the workspace should have a LandArea_A polygon feature class.
      in_extent_polygon (Feature Layer):
          The extent polygon in which the land area polygons will be generated.
      in_configuration_file {File}:
          The location of an .xml configuration file that lists the feature
          classes that will participate in defining the land topology edges and
          the feature classes that indicate areas where land should not exist.
          If not specified, the default GenerateLandAreasSettings.xml
          configuration file will be used.

        """