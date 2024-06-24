# Generated documentation for module arcpy.sa.Functions


class OptimalCorridorConnections(object):
    """
    Calculates the optimal corridor connections between two or more input regions.
    """

    @property
    def description(self) -> str:
        return """

        OptimalCorridorConnections_sa(in_regions, out_optimal_polygons, {in_barriers}, {in_cost_raster}, {out_optimal_lines}, {out_neighbor_polygons}, {out_neighbor_lines}, {corridor_method}, {corridor_width}, {distance_method})

        Calculates the optimal corridor connections between two or more input
        regions.

     INPUTS:
      in_regions (Raster Layer / Feature Layer):
          The input regions that will be connected by the optimal
          corridors.Regions can be defined by either a raster or a feature
          dataset.If the region input is a raster, the regions are defined by
          groups of
          contiguous (adjacent) cells of the same value. Each region must be
          uniquely numbered. The cells that are not part of any region must be
          NoData. The raster type must be integer, and the values can be either
          positive or negative.If the region input is a feature dataset, it can
          be polygons,
          polylines, or points. Polygon feature regions cannot be composed of
          multipart polygons.
      in_barriers {Raster Layer / Feature Layer}:
          The dataset that defines the barriers.The barriers can be defined by
          an integer or a floating-point raster,
          or by a point, line, or polygon feature.
      in_cost_raster {Raster Layer}:
          A raster defining the impedance or cost to move planimetrically
          through each cell.The value at each cell location represents the cost-
          per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      corridor_method {String}:
          Specifies how the corridor will be created.At this release, there is
          only one method to create corridors: fixed
          width. Since there is only a single default option, this parameter
          will be inactive, and will not appear on the tool dialog
          box.FIXED_WIDTH_CORRIDOR-The corridor will have a fixed width and the
          optimal corridors and paths will be created based on this width. This
          is the default.
      corridor_width {Double}:
          A linear distance that defines the width of the resulting corridors.
          The value must be greater than or equal to zero. The default is zero.
      distance_method {String}:
          Specifies whether the distance will be calculated using a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.GEODESIC-The distance calculation will be performed on the
          ellipsoid.
          Regardless of input or output projection, the results will not change.

     OUTPUTS:
      out_optimal_polygons (Feature Dataset):
          The output polygon or line feature class of the optimal corridors that
          connect each of the input regions. Corridors (or lines) will overlap
          in locations where corridors travel the same route.Each corridor (or
          line) is uniquely numbered and additional fields in
          the attribute table store specific information about the path. Those
          additional fields are the following:CORR_ID-The unique identifier for
          the corridorREGION1-The first region
          the path connectsREGION2-The other region the path connects
      out_optimal_lines {Feature Dataset}:
          The output line feature class identifies the optimal lines to connect
          each of the input regions. Lines will overlap in locations where paths
          travel the same route. Each path (or line) is uniquely numbered
          and additional fields
          in the attribute table store specific information about the path.
          Those additional fields are the following:        PATHID-The unique
          identifier for the pathPATHCOST-The total
          accumulative distance or cost for the pathREGION1-The first region the
          path connectsREGION2-The other region the path connects
      out_neighbor_polygons {Feature Dataset}:
          The output polygon or line feature class identifying the optimal
          corridors that connect each region to each of its closest or cost
          neighbors. Corridors (or lines) will overlap in locations where
          corridors travel the same route. Each corridor is uniquely
          numbered and additional fields in
          the attribute table store specific information about the path. Those
          additional fields are the following:        CORRIDORID-The unique
          identifier for the corridorREGION1-The first
          region the path connectsREGION2-The other region the path connects
      out_neighbor_lines {Feature Dataset}:
          The output line feature class identifying the optimal line from each
          region to each of its closest or cost neighbors. Each corridor
          (or polygon) is uniquely numbered and additional
          fields in the attribute table store specific information about the
          path. Those additional fields are the following:        PATHID-The
          unique identifier for the pathPATHCOST-The total
          accumulative distance or cost for the pathREGION1-The first region the
          path connectsREGION2-The other region the path connectsSince each path
          is represented by a unique line, there will be
          multiple lines in locations where the same route is optimal.

        """