# Generated documentation for module arcpy.cartography


class SmoothPolygon(object):
    """
    Smooths sharp angles in polygon outlines to improve aesthetic or cartographic quality.
    """

    @property
    def description(self) -> str:
        return """

        SmoothPolygon_cartography(in_features, out_feature_class, algorithm, tolerance, {endpoint_option}, {error_option}, {in_barriers;in_barriers...})

        Smooths sharp angles in polygon outlines to improve aesthetic or
        cartographic quality.

     INPUTS:
      in_features (Feature Layer):
          The polygon features to be smoothed.
      algorithm (String):
          Specifies the smoothing algorithm.PAEK-This is the acronym for
          Polynomial Approximation with Exponential
          Kernel. A smoothed polygon that will not pass through the input
          polygon vertices will be calculated. This is the
          default.BEZIER_INTERPOLATION-Bezier curves will be fitted between
          vertices.
          The resulting polygons pass through the vertices of the input
          polygons. This algorithm does not require a tolerance. Bezier curves
          will be approximated in the output.
      tolerance (Linear Unit):
          Sets a tolerance used by the PAEK algorithm. A tolerance must be
          specified, and it must be greater than zero. You can choose a
          preferred unit; the default is the feature unit. You must enter a 0 as
          a placeholder when using the BEZIER_INTERPOLATION smoothing algorithm.
      endpoint_option {Boolean}:
          This is a legacy parameter that is no longer used. It was formerly
          used to specify whether the endpoint of an isolated polygon ring would
          be preserved. This parameter is still included in the tool's syntax
          for compatibility in scripts and models but is hidden from the tool's
          dialog box.Specifies whether the endpoints of isolated polygon rings
          will be
          preserved. This option works with the PAEK algorithm
          only.FIXED_ENDPOINT-The endpoint of an isolated polygon ring will be
          preserved. This is the default.NO_FIXED-The endpoint of an isolated
          polygon ring will not be
          preserved; it will be smoothed.
      error_option {String}:
          Specifies how topological errors (possibly introduced in the process,
          such as line crossing or overlapping) will be
          handled.NO_CHECK-Topological errors will not be identified. This is
          the
          default.FLAG_ERRORS-If topological errors are found, they will be
          flagged.RESOLVE_ERRORS-If topological errors are found, they will be
          resolved.
      in_barriers {Feature Layer}:
          Inputs containing features that will act as barriers for smoothing.
          The resulting smoothed polygons will not touch or cross barrier
          features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class to be created.

        """