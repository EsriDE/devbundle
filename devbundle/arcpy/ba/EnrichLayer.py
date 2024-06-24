# Generated documentation for module arcpy.ba


class EnrichLayer(object):
    """
    Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations.
    """

    @property
    def description(self) -> str:
        return """

        EnrichLayer_ba(in_features, out_feature_class, {variables;variables...}, {buffer_type}, {distance}, {unit})

        Enriches data by adding demographic and landscape facts about the
        people and places that surround or are inside data locations.

     INPUTS:
      in_features (Feature Layer):
          The features that will be enriched.
      variables {String}:
          One or more variables that will be summarized and added to the output
          feature class.
      buffer_type {String}:
          Defines the area that will be enriched. The default value is Straight
          Line.When you're signed in to ArcGIS Online, travel mode options are
          dynamically populated. Input line features can only use the Straight
          Line distance method.
      distance {Double}:
          The distance or size of an area to enrich, for example, a 1-mile
          buffer or 5-minute walk time. Units correspond to the polygon type.
          The default value is 1.
      unit {String}:
          The units associated with the distance parameter. The default value is
          Kilometers.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output layer containing both the input attributes and user-
          selected attributes. Selected attributes are summarized from
          underlying demographic boundaries. Only the area inside the input
          boundary is considered.

        """