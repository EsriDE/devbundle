# Generated documentation for module arcpy.analysis


class Near(object):
    """
    Calculates distance and additional proximity information between the input features and the closest feature in another layer or feature class.
    """

    @property
    def description(self) -> str:
        return """

        Near_analysis(in_features, near_features;near_features..., {search_radius}, {location}, {angle}, {method}, {field_names;field_names...}, {distance_unit})

        Calculates distance and additional proximity information between the
        input features and the closest feature in another layer or feature
        class.

     INPUTS:
      in_features (Feature Layer):
          The input features, which can be point, polyline, polygon, or
          multipoint type.
      near_features (Feature Layer):
          One or more feature layers or feature classes containing near
          feature candidates. The near features can be point, polyline, polygon,
          or multipoint. If multiple layers or feature classes are specified,
          thefield will be added to the input table and will store the paths of
          the source feature class containing the nearest feature found. The
          same feature class or layer can be used as both input features and
          near features. NEAR_FC
      search_radius {Linear Unit}:
          The radius that will be used to search for near features. If no value
          is specified, all near features will be considered. If a distance but
          no unit or unknown is specified, the units of the coordinate system of
          the input features will be used. If the GEODESIC option is used for
          the method parameter, use a linear unit such as kilometers or miles.
      location {Boolean}:
          Specifies whether x- and y-coordinates of the closest location
          of the near feature will be written to theandfields.
          NEAR_XNEAR_YNO_LOCATION-Location information will not be written.
          This is the
          default.LOCATION-Location information will be written.
      angle {Boolean}:
          Specifies whether the near angle will be calculated and
          written to thefield in the output table. A near angle measures
          direction of the line connecting an input feature to its nearest
          feature at their closest locations. When the PLANAR method is used for
          the method parameter, the angle will be within the range of -180° to
          180°, with 0° to the east, 90° to the north, 180° (or -180°) to the
          west, and -90° to the south. When the GEODESIC method is used, the
          angle will be within the range of -180° to 180°, with 0° to the north,
          90° to the east, 180° (or -180°) to the south, and -90° to the west.
          NEAR_ANGLENO_ANGLE-The near angle value will not be calculated or
          written. This
          is the default. ANGLE-The near angle value will be calculated
          and written to
          thefield. NEAR_ANGLE
      method {String}:
          Specifies whether a shortest path on a spheroid (geodesic) or a flat
          earth (planar) distance method will be used. It is recommended that
          you use the GEODESIC method for data stored in a coordinate system
          that is not appropriate for distance measurements (for example, Web
          Mercator or any geographic coordinate system) and for a dataset that
          spans a large geographic area.PLANAR-Planar distance will be used
          between features. This is the
          default.GEODESIC-Geodesic distance will be used between features. This
          method
          takes into account the curvature of the spheroid and correctly deals
          with data near the international date line and the poles.
      field_names {Value Table}:
          The names of the attribute fields that will be added during
          processing.If this parameter is not used or any fields that will be
          added are
          excluded from this parameter, the default field names will be used.
          By default,andfields will be added,andfields will be added
          when the location parameter is set to LOCATION, thefield will be added
          when the angle parameter is set to ANGLE, and thefield will be added
          when multiple inputs are used.
          NEAR_FIDNEAR_DISTNEAR_XNEAR_YNEAR_ANGLENEAR_FC
      distance_unit {String}:
          Specifies the unit of measurement for thefiled. When no unit
          of measurement is specified, the values in thefield will be in the
          linear unit of the input feature's coordinate system. If the input is
          in a geographic coordinate system and the geodesic method is used, the
          units of thefield will be meters.
          NEAR_DISTNEAR_DISTNEAR_DISTKilometers-The unit will be
          kilometers.Meters-The unit will be
          meters.NauticalMilesInt-The unit will be international nautical
          miles.MilesInt-The unit will be statute miles.YardsInt-The unit will
          be international yards.FeetInt-The unit will be international
          feet.NauticalMiles-The unit will be U.S. survey nautical
          miles.Miles-The unit will be U.S. survey miles.Yards-The unit will be
          U.S. survey yards.Feet-The unit will be U.S. survey feet.

        """