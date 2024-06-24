# Generated documentation for module arcpy.aviation


class GenerateDerivedAirspaceGeometry(object):
    """
    Generates airspace geometry for associated airspace features from an imported AIXM 5.1 message.
    """

    @property
    def description(self) -> str:
        return """

        GenerateDerivedAirspaceGeometry_aviation(in_airspace_features, airspace_association_table, {airspace_part_features})

        Generates airspace geometry for associated airspace features from an
        imported AIXM 5.1 message.

     INPUTS:
      in_airspace_features (Feature Layer):
          The input polygon feature class containing three or more airspace
          features, some or all of which will be used to derive more complex
          airspace features. The derived features will be updated in this input
          feature class.
      airspace_association_table (Table View):
          The input table containing information about the geometric
          associations between two or more airspace features. The airspace
          relationship information stored in this table is populated through the
          AIXM import process.
      airspace_part_features {Feature Layer}:
          The feature class that will be updated with airspace features derived
          from the in_airspace_features parameter.

        """