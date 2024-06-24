# Generated documentation for module arcpy.intelligence


class GenerateCoverageAreas(object):
    """
    Creates a proximity buffer for input Intelligence, Surveillance, and Reconnaissance (ISR) or patrol assets for use in the Generate Blind Spot Areas tool.
    """

    @property
    def description(self) -> str:
        return """

        GenerateCoverageAreas_intelligence(in_features, out_feature_class, buffer_type, {range_unit}, {start_time_field}, {end_time_field})

        Creates a proximity buffer for input Intelligence, Surveillance, and
        Reconnaissance (ISR) or patrol assets for use in the Generate Blind
        Spot Areas tool.

     INPUTS:
      in_features (Feature Layer):
          The input asset features.
      buffer_type (Linear Unit / Field):
          The distance around the input features that will be buffered.
          Distances can be provided as either a linear distance or a field from
          the in_features parameter value that defines the individual ranges and
          units to buffer each feature.
      range_unit {String}:
          Specifies the linear unit that will be used when the chosen
          buffer_type parameter value does not contain the unit of
          distance.Meters-The distance unit will be meters.Kilometers-The
          distance unit
          will be kilometers.Feet-The distance unit will be feet.Miles-The
          distance unit will be miles.NauticalMiles-The distance unit will be
          nautical miles.
      start_time_field {Field}:
          The field containing the start date and time the asset is available.
      end_time_field {Field}:
          The field containing the end date and time the asset is no longer
          available.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output blind spot buffer features.

        """