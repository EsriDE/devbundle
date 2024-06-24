# Generated documentation for module arcpy.sa.Functions


class AddSurfaceInformation(object):
    """
    Attributes input features with height-based statistical information derived from the overlapping portions of a surface.
    """

    @property
    def description(self) -> str:
        return """

        AddSurfaceInformation_sa(in_feature_class, in_surface, out_property;out_property..., {method}, {sample_distance}, {z_factor}, {pyramid_level_resolution}, {noise_filtering})

        Attributes input features with height-based statistical information
        derived from the overlapping portions of a surface.

     INPUTS:
      in_feature_class (Feature Layer):
          The point, multipoint, polyline, or polygon features that define the
          locations for determining one or more surface properties.
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / LAS Dataset Layer / Terrain Layer / Image Service):
          The LAS dataset, mosaic, raster, terrain, or TIN surface used for
          interpolating z-values.
      out_property (String):
          Specifies the surface elevation properties that will be added to the
          attribute table of the input feature class.Z-The surface z-values
          interpolated for the x,y-location of each
          single-point feature will be added.Z_MIN-The lowest surface z-values
          in the area defined by the polygon,
          along the length of a line, or among the interpolated values for
          points in a multipoint record will be added.Z_MAX-The highest surface
          elevation in the area defined by the
          polygon, along the length of a line, or among the interpolated values
          for points in a multipoint record will be added.Z_MEAN-The average
          surface elevation of the area defined by the
          polygon, along the length of a line, or among the interpolated values
          for points in a multipoint record will be added.SURFACE_AREA-The 3D
          surface area for the region defined by each
          polygon will be added.SURFACE_LENGTH-The 3D distance of the line along
          the surface will be
          added.MIN_SLOPE-The slope value closest to zero along the line or
          within the
          area defined by the polygon will be added.MAX_SLOPE-The highest slope
          value along the line or within the area
          defined by the polygon will be added.AVG_SLOPE-The average slope value
          along the line or within the area
          defined by the polygon will be added.
      method {String}:
          Specifies the interpolation method that will be used to determine
          information about the surface.BILINEAR-An interpolation method
          exclusive to the raster surface that
          determines cell values from the four nearest cells will be used. This
          is the only option available for a raster surface.LINEAR-Elevation
          will be obtained from the plane defined by the
          triangle that contains the x,y-location of a query point. This is the
          default interpolation method for TINs, terrains, and LAS
          datasets.NATURAL_NEIGHBORS-Elevation will be obtained by applying
          area-based
          weights to the natural neighbors of a query point.CONFLATE_ZMIN-
          Elevation will be obtained from the smallest z-value
          found among the natural neighbors of a query point.CONFLATE_ZMAX-
          Elevation will be obtained from the largest z-value
          found among the natural neighbors of a query point.CONFLATE_NEAREST-
          Elevation will be obtained from the nearest value
          among the natural neighbors of a query point.CONFLATE_CLOSEST_TO_MEAN-
          Elevation will be obtained from the z-value
          that is closest to the average of all the natural neighbors of a query
          point.
      sample_distance {Double}:
          The spacing at which z-values will be interpolated. By default, the
          raster cell size is used when the input surface is a raster, and the
          natural densification of the triangulated surface is used when the
          input is a terrain or TIN dataset.
      z_factor {Double}:
          The factor by which z-values will be multiplied. This is typically
          used to convert z linear units to match x,y linear units. The default
          is 1, which leaves elevation values unchanged. This parameter is not
          available if the spatial reference of the input surface has a z-datum
          with a specified linear unit.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level
          that will be used. The default is 0, or full resolution.
      noise_filtering {String}:
          Defines whether portions of the surface that are potentially
          characterized by anomalous measurements will be excluded from
          contributing to slope calculations. Other properties are not affected
          by this parameter.Line features offer a length filter in which line
          segments with 3D
          lengths that are shorter than the specified value will be excluded
          from slope calculations. Polygon features offer an area filter in
          which polygons covering a surface area smaller than the specified
          value will be excluded.

        """