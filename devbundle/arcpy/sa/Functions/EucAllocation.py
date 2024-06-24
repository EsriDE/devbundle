# Generated documentation for module arcpy.sa.Functions


class EucAllocation(object):
    """
    Calculates, for each cell, the nearest source based on Euclidean distance.
    """

    @property
    def description(self) -> str:
        return """

        EucAllocation_sa(in_source_data, {maximum_distance}, {in_value_raster}, {cell_size}, {source_field}, {out_distance_raster}, {out_direction_raster}, {distance_method}, {in_barrier_data}, {out_back_direction_raster})

        Calculates, for each cell, the nearest source based on Euclidean
        distance.

     INPUTS:
      in_source_data (Composite Geodataset):
          The input source locations.This is a raster or feature identifying the
          cells or locations that
          will be used to calculate the Euclidean distance for each output cell
          location.For rasters, the input type can be integer or floating
          point.If the input source raster is floating point, the
          in_value_raster
          parameter must be set, and it must integer. The value raster will take
          precedence over the source_field parameter setting.
      maximum_distance {Double}:
          The threshold that the accumulative distance values cannot exceed.If
          an accumulative Euclidean distance value exceeds this value, the
          output value for the cell location will be NoData.The default distance
          is to the edge of the output raster.
      in_value_raster {Composite Geodataset}:
          The input integer raster that identifies the zone values that will be
          used for each input source location.For each source location (cell or
          feature), the in_value_raster value
          will be assigned to all cells allocated to the source location for the
          computation. The value raster will take precedence over the
          source_field parameter setting.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      source_field {Field}:
          The field used to assign values to the source locations. It must be of
          integer type.If the in_value_raster parameter has been set, the values
          in that
          input will have precedence over the source_field parameter setting.
      distance_method {String}:
          Specifies whether the distance will be calculated using a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.GEODESIC-The distance calculation will be performed on the
          ellipsoid.
          Regardless of input or output projection, the results will not change.
      in_barrier_data {Composite Geodataset}:
          The dataset that defines the barriers.The barriers can be defined by
          an integer or a floating-point raster,
          or by a point, line, or polygon feature.

     OUTPUTS:
      out_allocation_raster (Raster Dataset):
          The output Euclidean allocation raster.The cell values (zones)
          identify the nearest source location.The output raster is of integer
          type.
      out_distance_raster {Raster Dataset}:
          The output Euclidean distance raster.The distance raster identifies,
          for each cell, the Euclidean distance
          to the closest source cell, set of source cells, or source
          location.The output raster is of floating-point type.
      out_direction_raster {Raster Dataset}:
          The output Euclidean direction raster.The direction raster contains
          the calculated direction, in degrees,
          that each cell center is from the closest source cell center.The range
          of values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).The output
          raster is of integer type.
      out_back_direction_raster {Raster Dataset}:
          The output Euclidean back direction raster.The back direction raster
          contains the calculated direction in
          degrees. The direction identifies the next cell along the shortest
          path back to the closest source while avoiding barriers.The range of
          values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).The output
          raster is of type float.

        """