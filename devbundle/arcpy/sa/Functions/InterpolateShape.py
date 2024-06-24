# Generated documentation for module arcpy.sa.Functions


class InterpolateShape(object):
    """
    Creates 3D features by interpolating z-values from a surface.
    """

    @property
    def description(self) -> str:
        return """

        InterpolateShape_sa(in_surface, in_feature_class, out_feature_class, {sample_distance}, {z_factor}, {method}, {vertices_only}, {pyramid_level_resolution}, {preserve_features})

        Creates 3D features by interpolating z-values from a surface.

     INPUTS:
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer / Image Service):
          The surface that will be used for interpolating z-values.
      in_feature_class (Feature Layer):
          The input features that will be processed.
      sample_distance {Double}:
          The spacing at which z-values will be interpolated. By default, this
          is a raster dataset's cell size or a triangulated surface's natural
          densification.
      z_factor {Double}:
          The factor by which z-values will be multiplied. This is typically
          used to convert z linear units to match x,y linear units. The default
          is 1, which leaves elevation values unchanged. This parameter is not
          available if the spatial reference of the input surface has a z-datum
          with a specified linear unit.
      method {String}:
          Specifies the interpolation method that will be used to determine
          elevation values for the output features. The available options depend
          on the surface type.BILINEAR-The value of the query point will be
          determined using
          bilinear interpolation. This is the default when the input is a raster
          surface.NEAREST-The value of the query point will be determined using
          nearest
          neighbor interpolation. With this method, surface values will only be
          interpolated for the input feature's vertices. This option is only
          available for a raster surface.LINEAR-Elevation values will be
          obtained from the plane defined by the
          triangle that contains the x,y-location of a query point. This is the
          default interpolation method for TIN, terrain, and LAS
          datasets.NATURAL_NEIGHBORS-Elevation values will be obtained by
          applying area-
          based weights to the natural neighbors of a query point.CONFLATE_ZMIN-
          Elevation values will be obtained from the smallest
          z-value found among the natural neighbors of a query
          point.CONFLATE_ZMAX-Elevation values will be obtained from the largest
          z-value found among the natural neighbors of a query
          point.CONFLATE_NEAREST-Elevation values will be obtained from the
          nearest
          value among the natural neighbors of a query
          point.CONFLATE_CLOSEST_TO_MEAN-Elevation values will be obtained from
          the
          z-value that is closest to the average of all the natural neighbors of
          a query point.
      vertices_only {Boolean}:
          Specifies whether the interpolation will only occur along the vertices
          of an input feature, ignoring the sample distance
          option.DENSIFY-Interpolation will occur using the sampling distance.
          This is
          the default.VERTICES_ONLY-Interpolation will only occur along the
          vertices.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level
          that will be used. The default is 0, or full resolution.
      preserve_features {Boolean}:
          Specifies whether features with one or more vertices that fall outside
          the raster's data area will be retained in the output. This parameter
          is only available when the input surface is a raster and the nearest
          neighbor interpolation method is used.PRESERVE-Each vertex that falls
          outside the raster surface will have
          its z-value derived from the trend of z-values calculated for the
          vertices within the raster surface and will be retained in the
          output.EXCLUDE-Features with at least one vertex that falls outside
          the
          raster surface will be skipped in the output. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced.

        """