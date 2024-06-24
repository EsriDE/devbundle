# Generated documentation for module arcpy.cartography


class SimplifyPolygon(object):
    """
    Simplifies polygons by removing relatively extraneous vertices while preserving essential shape.
    """

    @property
    def description(self) -> str:
        return """

        SimplifyPolygon_cartography(in_features, out_feature_class, algorithm, tolerance, {minimum_area}, {error_option}, {collapsed_point_option}, {in_barriers;in_barriers...})

        Simplifies polygons by removing relatively extraneous vertices while
        preserving essential shape.

     INPUTS:
      in_features (Feature Layer):
          The input polygon features that will be simplified.
      algorithm (String):
          Specifies the polygon simplification algorithm that will be
          used.POINT_REMOVE-Critical points that preserve the essential shape of
          a
          polygon outline will be retained, and all other points will be removed
          (Douglas-Peucker). This is the default.BEND_SIMPLIFY-Critical bends
          will be retained, and extraneous bends
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
      minimum_area {Areal Unit}:
          The minimum area for a polygon to be retained. The default value is
          zero, that is, to keep all polygons. You can choose a preferred unit
          for the specified value; otherwise, the units of the input will be
          used.
      error_option {String}:
          Specifies how topological errors will be handled. Topological errors
          may be introduced in the simplification process and can include lines
          crossing or overlapping lines.NO_CHECK-Topological errors will not be
          identified. This is the
          default.FLAG_ERRORS-Topological errors will be
          flagged.RESOLVE_ERRORS-Topological errors will be resolved.
      collapsed_point_option {Boolean}:
          Specifies whether an output point feature class will be created to
          store the centers of polygons that are removed because they are
          smaller than the minimum_area parameter value. The point output is
          derived; it will use the same name and location as the
          out_feature_class parameter value but with a _Pnt
          suffix.KEEP_COLLAPSED_POINTS-A derived output point feature class will
          be
          created to store the centers of polygons that are removed because they
          are smaller than the minimum area. This is the default.NO_KEEP-A
          derived output point feature class will not be created.
      in_barriers {Feature Layer}:
          The inputs containing features to act as barriers for simplification.
          Resulting simplified polygons will not touch or cross barrier
          features. For example, when simplifying forested areas, the resulting
          simplified forest polygons will not cross road features defined as
          barriers.

     OUTPUTS:
      out_feature_class (Feature Class):
          The simplified output polygon feature class. It will contain all the
          fields from the input feature class. The output polygon feature class
          is topologically correct. The tool does not introduce topology errors,
          but topological errors in the input data will be flagged in the output
          polygon feature class. The output feature class will include
          theandfields to contain
          the input feature IDs and the input topological errors or
          discrepancies, respectively. InPoly_FIDSimPgnFlag
          Theattribute values are as follows:
          SimPgnFlagSimPgnFlag = 0 indicates that no errors are
          present.SimPgnFlag = 1
          indicates a topological error is present.SimPgnFlag = 2 indicates
          features that have been split by a partition
          and are now smaller than the minimum area after simplification. The
          flag may appear on only one part of the split feature. These features
          will be retained in the output feature class. This situation occurs
          only when the Cartographic Partitions environment setting is used.

        """