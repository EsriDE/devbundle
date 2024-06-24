# Generated documentation for module arcpy.cartography


class SimplifyLine(object):
    """
    Simplifies lines by removing relatively extraneous vertices while preserving essential shape.
    """

    @property
    def description(self) -> str:
        return """

        SimplifyLine_cartography(in_features, out_feature_class, algorithm, tolerance, {error_resolving_option}, {collapsed_point_option}, {error_checking_option}, {in_barriers;in_barriers...}, {error_option})

        Simplifies lines by removing relatively extraneous vertices while
        preserving essential shape.

     INPUTS:
      in_features (Feature Layer):
          The input line features that will be simplified.
      algorithm (String):
          Specifies the line simplification algorithm that will be
          used.POINT_REMOVE-Critical points that preserve the essential shape of
          a
          line will be retained, and all other points will be removed (Douglas-
          Peucker). This is the default.BEND_SIMPLIFY-Critical bends will be
          retained, and extraneous bends
          will be removed from a line (Wang-Müller).WEIGHTED_AREA-Vertices that
          form triangles of effective area that have
          been weighted by triangle shape will be retained (Zhou-
          Jones).EFFECTIVE_AREA-Vertices that form triangles of effective area
          will be
          retained (Visvalingam-Whyatt).
      tolerance (Linear Unit):
          The degree of simplification that will be used. You can choose
          a preferred unit; otherwise, the units of the input will be used.
          Theandfields will be added to the output to store the tolerance that
          was used when processing occurred. MinSimpTolMaxSimpTolFor the
          POINT_REMOVE algorithm, the tolerance is the maximum allowable
          perpendicular distance between each vertex and the newly created
          line.For the BEND_SIMPLIFY algorithm, the tolerance is the diameter of
          a
          circle that approximates a significant bend.For the WEIGHTED_AREA
          algorithm, the square of the tolerance is the
          area of a significant triangle defined by three adjacent vertices. The
          further a triangle deviates from equilateral, the higher weight it is
          given, and the less likely it is to be removed.For the EFFECTIVE_AREA
          algorithm, the square of the tolerance is the
          area of a significant triangle defined by three adjacent vertices.
      error_resolving_option {Boolean}:
          Resolve topological errors
      collapsed_point_option {Boolean}:
          Specifies whether an output point feature class will be created to
          store the endpoints of lines that are smaller than the spatial
          tolerance. The point output is derived; it will use the same name and
          location as the out_feature_class parameter value but with a _Pnt
          suffix.KEEP_COLLAPSED_POINTS-A derived output point feature class will
          be
          created to store the endpoints of collapsed zero length lines. This is
          the default.NO_KEEP-A derived output point feature class will not be
          created.
      error_checking_option {Boolean}:
          Check for topological errors
      in_barriers {Feature Layer}:
          Inputs containing features to act as barriers for simplification.
          Resulting simplified lines will not touch or cross barrier features.
          For example, when simplifying contour lines, spot height features
          input as barriers ensure that the simplified contour lines will not
          simplify across these points. The output will not violate the
          elevation as described by measured spot heights.
      error_option {String}:
          Specifies how topological errors will be handled. Topological errors
          may be introduced in the simplification process and can include lines
          crossing or overlapping lines.NO_CHECK-Topological errors will not be
          identified. This is the
          default.FLAG_ERRORS-Topological errors will be
          flagged.RESOLVE_ERRORS-Topological errors will be resolved.

     OUTPUTS:
      out_feature_class (Feature Class):
          The simplified output line feature class. It will contain all
          the fields from the input feature class. The output line feature class
          is topologically correct. The tool does not introduce topology errors,
          but topological errors in the input data will be flagged in the output
          line feature class. The output feature class will include theandfields
          to contain the input feature IDs and the input topological errors,
          respectively. Avalue of 1 indicates that an input topological error is
          present; a value of 0 (zero) indicates that no input error is present.
          InLine_FIDSimLnFlagSimLnFlag

        """