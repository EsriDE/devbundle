# Generated documentation for module arcpy.analysis


class GenerateNearTable(object):
    """
    Calculates distances and other proximity information between features in one or more feature classes or layers. Unlike the Near tool, which modifies the input, Generate Near Table writes results to a new stand- alone table and supports finding more than one near feature.
    """

    @property
    def description(self) -> str:
        return """

        GenerateNearTable_analysis(in_features, near_features;near_features..., out_table, {search_radius}, {location}, {angle}, {closest}, {closest_count}, {method}, {distance_unit})

        Calculates distances and other proximity information between features
        in one or more feature classes or layers. Unlike the Near tool, which
        modifies the input, Generate Near Table writes results to a new stand-
        alone table and supports finding more than one near feature.

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
          Specifies whether x- and y-coordinates of the input feature's
          location and closest location of the near feature will be written to
          the,,, andfields. FROM_XFROM_YNEAR_XNEAR_YNO_LOCATION-
          Locations will not be written to the output table. This
          is the default.LOCATION-Locations will be written to the output
          table.
      angle {Boolean}:
          Specifies whether the near angle will be calculated and
          written to thefield in the output table. A near angle measures
          direction of the line connecting an input feature to its nearest
          feature at their closest locations. When the PLANAR method is used for
          the method parameter, the angle will be within the range of -180° to
          180°, with 0° to the east, 90° to the north, 180° (or -180°) to the
          west, and -90° to the south. When the GEODESIC method is used for the
          method parameter, the angle will be within the range of -180° to 180°,
          with 0° to the north, 90° to the east, 180° (or -180°) to the south,
          and -90° to the west. NEAR_ANGLE         NO_ANGLE-The near
          angle will not be calculated and thefield
          will not be added to the output table. This is the default.
          NEAR_ANGLE         ANGLE-The near angle will be calculated and
          thefield will be
          added to the output table. NEAR_ANGLE
      closest {Boolean}:
          Specifies whether only the closest near feature will be written to the
          output table.CLOSEST-Only the closest near feature will be written to
          the output
          table. This is the default.ALL-Multiple near features will be written
          to the output table (a
          limit can be specified in the closest_count parameter).
      closest_count {Long}:
          Limits the number of near features reported for each input feature.
          This parameter is ignored if the closest parameter is set to CLOSEST.
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

     OUTPUTS:
      out_table (Table):
          The output table containing the result of the analysis.

        """