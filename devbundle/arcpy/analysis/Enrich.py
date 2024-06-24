# Generated documentation for module arcpy.analysis


class Enrich(object):
    """
    Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations. The output is a duplicate of your input with additional attribute fields. This tool requires an ArcGIS Online organizational account or a locally installed Business Analyst dataset.
    """

    @property
    def description(self) -> str:
        return """

        Enrich_analysis(in_features, out_feature_class, {variables;variables...}, {buffer_type}, {distance}, {unit})

        Enriches data by adding demographic and landscape facts about the
        people and places that surround or are inside data locations. The
        output is a duplicate of your input with additional attribute fields.
        This tool requires an ArcGIS Online organizational account or a
        locally installed Business Analyst dataset.

     INPUTS:
      in_features (Feature Layer):
          The features to be enriched.
      variables {String}:
          The variables to be summarized and added to the output feature class.
      buffer_type {String}:
          Input point features must have an associated boundary polygon
          to enrich. When connected to ArcGIS Online, travel mode options are
          dynamically populated. Input line features can only usedistance. The
          default value is. Straight LineStraight Line
      distance {Double}:
          Determines the distance or size of an area to enrich (for example, a
          1-mile buffer or 5-minute walk time). Units correspond to the buffer
          type. The default value is 1.
      unit {String}:
          The units associated with the distance or time parameter.Miles-MilesYa
          rds-YardsFeet-FeetKilometers-KilometersMeters-MetersHours
          -HoursMinutes-MinutesSeconds-Seconds

     OUTPUTS:
      out_feature_class (Feature Class):
          A new layer containing both the input attributes and user-selected
          attributes. User-selected attributes are summarized from underlying
          demographic boundaries. Only the area inside the input boundary is
          considered.

        """