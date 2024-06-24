# Generated documentation for module arcpy.sa.Functions


class Idw(object):
    """
    Interpolates a raster surface from points using an inverse distance weighted (IDW) technique.
    """

    @property
    def description(self) -> str:
        return """

        Idw_sa(in_point_features, z_field, {cell_size}, {power}, {search_radius}, {in_barrier_polyline_features})

        Interpolates a raster surface from points using an inverse distance
        weighted (IDW) technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated
          into a surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This
          can be a numeric field or the Shape field if the input point
          features contain z-values.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      power {Double}:
          The exponent of distance.Controls the significance of surrounding
          points on the interpolated
          value. A higher power results in less influence from distant points.
          It can be any real number greater than 0, but the most reasonable
          results will be obtained using values from 0.5 to 3. The default is 2.
      search_radius {Radius}:
          The Radius class defines which of the input points will be used to
          interpolate the value for each cell in the output raster.There are two
          types of radius classes: RadiusVariable and RadiusFixed.
          A Variable search radius is used to find a specified number of input
          sample points for the interpolation. The Fixed type uses a specified
          fixed distance within which all input points will be used for the
          interpolation. The Variable type is the default.
          RadiusVariable ({numberofPoints}, {maxDistance})
          {numberofPoints}-An integer value specifying the number of nearest
          input sample points to be used to perform interpolation. The default
          is 12 points.{maxDistance}-Specifies the distance, in map units, by
          which to limit
          the search for the nearest input sample points. The default value is
          the length of the extent's diagonal. RadiusFixed ({distance},
          {minNumberofPoints})
          {distance}-Specifies the distance as a radius within which
          input sample points will be used to perform the interpolation.
          The value of the radius is expressed in map units. The default radius
          is five times the cell size of the output raster.
          {minNumberofPoints}-An integer defining the minimum number
          of points to be used for interpolation. The default value is 0.
          If the required number of points is not found within the specified
          distance, the search distance will be increased until the specified
          minimum number of points is found.When the search radius needs to be
          increased it is done so until the
          {minNumberofPoints} fall within that radius, or the extent of the
          radius crosses the lower (southern) and/or upper (northern) extent of
          the output raster. NoData is assigned to all locations that do not
          satisfy the above condition.
      in_barrier_polyline_features {Composite Geodataset}:
          Polyline features to be used as a break or limit in searching for the
          input sample points.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.

        """