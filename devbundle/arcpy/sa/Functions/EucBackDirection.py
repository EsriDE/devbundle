# Generated documentation for module arcpy.sa.Functions


class EucBackDirection(object):
    """
    Calculates, for each cell, the direction, in degrees, to the neighboring cell along the shortest path back to the closest source while avoiding barriers.
    """

    @property
    def description(self) -> str:
        return """

        EucBackDirection_sa(in_source_data, {in_barrier_data}, {maximum_distance}, {cell_size}, {distance_method})

        Calculates, for each cell, the direction, in degrees, to the
        neighboring cell along the shortest path back to the closest source
        while avoiding barriers.

     INPUTS:
      in_source_data (Composite Geodataset):
          The input source locations.This is a raster or feature dataset that
          identifies the cells or
          locations to which the Euclidean back direction for every output cell
          location is calculated.For rasters, the input type can be integer or
          floating point.
      in_barrier_data {Composite Geodataset}:
          The dataset that defines the barriers.The barriers can be defined by
          an integer or a floating-point raster,
          or by a point, line, or polygon feature.
      maximum_distance {Double}:
          The threshold that the accumulative distance values cannot exceed.If
          an accumulative Euclidean distance value exceeds this value, the
          output value for the cell location will be NoData.The default distance
          is to the edge of the output raster.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      distance_method {String}:
          Specifies whether the distance will be calculated using a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.GEODESIC-The distance calculation will be performed on the
          ellipsoid.
          Regardless of input or output projection, the results will not change.

     OUTPUTS:
      out_back_direction_raster (Raster Dataset):
          The output Euclidean back direction raster.The back direction raster
          contains the calculated direction in
          degrees. The direction identifies the next cell along the shortest
          path back to the closest source while avoiding barriers.The range of
          values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).The output
          raster is of type float.

        """