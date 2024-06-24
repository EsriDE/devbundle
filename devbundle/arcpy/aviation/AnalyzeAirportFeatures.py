# Generated documentation for module arcpy.aviation


class AnalyzeAirportFeatures(object):
    """
    Analyzes specified point features around an airfield to find and record information such as distance from a given runway centerline or the end of the nearest runway and its designation.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeAirportFeatures_aviation(in_features, in_runway_features, out_table, {in_features_height}, {in_features_height_unit}, {runway_end_features}, {airport_ref_point_features}, {ref_point_height}, {ref_point_height_unit}, {in_out_horizontal_unit})

        Analyzes specified point features around an airfield to find and
        record information such as distance from a given runway centerline or
        the end of the nearest runway and its designation.

     INPUTS:
      in_features (Feature Layer):
          The input point features that will be analyzed and recorded in terms
          of their physical relationships to features in the other inputs.
      in_runway_features (Feature Layer):
          The input runway polyline features, specifically their centerlines,
          that will be used in the analysis.
      in_features_height {String}:
          Specifies the name of a field in the input airport features
          dataset. The specified field must contain numeric values. The values
          in this field will be used to identify the height of each input
          airport feature. If thevalue is chosen as the location of the height,
          theparameter value will be ignored. SHAPE_ZInput Analysis
          Features Height UnitSHAPE_Z-Height values will be derived from the
          z-values of the input
          point features. This is the default.
      in_features_height_unit {String}:
          Specifies the linear unit of measure that will be used when the
          in_features_height parameter value is specified.KILOMETERS-The unit
          will be kilometers.METERS-The unit will be
          meters.DECIMETERS-The unit will be decimeters.CENTIMETERS-The unit
          will be centimeters.MILLIMETERS-The unit will be
          millimeters.NAUTICAL_MILES-The unit will be nautical miles.MILES-The
          unit will be miles.YARDS-The unit will be yards.FEET-The unit will be
          feet.INCHES-The unit will be inches.DECIMAL_DEGREES-The unit will be
          decimal degrees.POINTS-The unit will be points.UNKNOWN-The unit will
          be unknown.
      runway_end_features {Feature Layer}:
          The input runway end point features associated with the runways in the
          in_runway_features parameter that represent the thresholds of those
          runways.
      airport_ref_point_features {Feature Layer}:
          The input airport control point features that contain the
          runway threshold points. The runway threshold points will be
          identified by searching for theattribute equal to, and the
          attributeequal to the runway end designator.
          POINTTYPEDISPLACED_THRESHOLDRUNWAYENDD
      ref_point_height {String}:
          Specifies the name of a field in the input airport reference
          point features dataset. The specified field must contain numeric
          values. The values in this field will be used to identify the height
          of each input airport reference point feature. Ifis chosen as the
          location of the height, theparameter value will be ignored.
          SHAPE_ZAirport Control Point Elevation UnitSHAPE_Z-The z-value of each
          point will be used. This is the default.
      ref_point_height_unit {String}:
          Specifies the linear unit of measure that will be used when an airport
          reference point height is specified.KILOMETERS-The unit will be
          kilometers.METERS-The unit will be
          meters.DECIMETERS-The unit will be decimeters.CENTIMETERS-The unit
          will be centimeters.MILLIMETERS-The unit will be
          millimeters.NAUTICAL_MILES-The unit will be nautical miles.MILES-The
          unit will be miles.YARDS-The unit will be yards.FEET-The unit will be
          feet.INCHES-The unit will be inches.DECIMAL_DEGREES-The unit will be
          decimal degrees.POINTS-The unit will be points.UNKNOWN-The unit will
          be unknown.
      in_out_horizontal_unit {String}:
          Specifies the output unit of measurement for the five output distances
          produced.SAME_AS_INPUT-The horizontal units from the input coordinate
          system
          will be used. If the input data is not projected, this will be meters.
          This is the defaultKILOMETERS-The unit will be kilometers.METERS-The
          unit will be meters.DECIMETERS-The unit will be
          decimeters.CENTIMETERS-The unit will be centimeters.MILLIMETERS-The
          unit will be millimeters.NAUTICAL_MILES-The unit will be nautical
          miles.MILES-The unit will be miles.YARDS-The unit will be
          yards.FEET-The unit will be feet.INCHES-The unit will be inches.

     OUTPUTS:
      out_table (Table View):
          The output table, with a row for each input airport feature,
          containing the analyzed results. The EGL and MSL columns will no
          longer be output.

        """