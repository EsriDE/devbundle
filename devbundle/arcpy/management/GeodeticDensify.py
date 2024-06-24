# Generated documentation for module arcpy.management


class GeodeticDensify(object):
    """
    Creates new features by replacing input feature's segments with densified approximations of geodesic segments. Four type of geodesic segments can be constructed: Geodesic, Great Elliptic, Loxodrome, and Normal Section.
    """

    @property
    def description(self) -> str:
        return """

        GeodeticDensify_management(in_features, out_feature_class, geodetic_type, {distance})

        Creates new features by replacing input feature's segments with
        densified approximations of geodesic segments. Four type of geodesic
        segments can be constructed: Geodesic, Great Elliptic, Loxodrome, and
        Normal Section.

     INPUTS:
      in_features (Feature Layer):
          The input line or polygon features.
      geodetic_type (String):
          Specifies the type of geodetic segment to construct. Geodetic
          calculations are performed on the ellipsoid associated with the input
          data's coordinate system.GEODESIC-The shortest distance between two
          points on the surface of
          the spheroid (ellipsoid).LOXODROME-The line of equal azimuth (from a
          pole) connecting the two
          points.GREAT_ELLIPTIC-The line made by the intersection of a plane
          that
          contains the center of the spheroid and the two
          points.NORMAL_SECTION-The line made by the intersection of a plane
          that
          contains the center of the spheroid and is perpendicular to the
          surface at the first point.
      distance {Linear Unit}:
          The distance between vertices along the output geodesic segment. The
          default value is 50 kilometers.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the densified geodesic features.

        """