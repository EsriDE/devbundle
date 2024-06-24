# Generated documentation for module arcpy.sa.Functions


class RegionGroup(object):
    """
    For each cell in the output, the identity of the connected region to which that cell belongs is recorded. A unique number is assigned to each region.
    """

    @property
    def description(self) -> str:
        return """

        RegionGroup_sa(in_raster, {number_neighbors}, {zone_connectivity}, {add_link}, {excluded_value})

        For each cell in the output, the identity of the connected region to
        which that cell belongs is recorded. A unique number is assigned to
        each region.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster for which unique connected regions of cells will be
          identified.It must be of integer type.
      number_neighbors {String}:
          Specifies the number of neighboring cells to use when evaluating
          connectivity between cells that define a region.FOUR-Connectivity is
          evaluated for the four nearest (orthogonal)
          neighbors of each input cell. Only the cells with the same value that
          share at least one side will contribute to an individual region. If
          two cells with the same value are diagonal from one another, they are
          not considered connected. This is the default.EIGHT-Connectivity is
          evaluated for the eight nearest neighbors (both
          orthogonal and diagonal) of each input cell. Cells with the same value
          that are connected either along a common edge or corner to each other
          will contribute to an individual region.
      zone_connectivity {String}:
          Defines which cell values should be considered when testing for
          connectivity.WITHIN-Connectivity for a region is evaluated for input
          cells that are
          part of the same zone (cell value). The only cells that can be grouped
          are cells from the same zone that meet the spatial requirements of
          connectivity specified by the number_neighbors parameter (four or
          eight). This is the default.CROSS-Connectivity for a region is
          evaluated between cells of any
          value, except for the zone cells identified to be excluded by the
          excluded_value parameter, and subject to the spatial requirements
          specified by the number_neighbors parameter. Groupings of regions in
          the input that are separated from other groupings by a buffer of
          NoData cells will be processed independently from each other.
      add_link {Boolean}:
          Specifies whether a link field will be added to the table of the
          output when the zone_connectivity parameter is set to WITHIN. It is
          ignored if that parameter is set to CROSS. ADD_LINK-Afield
          will be added to the table of the output
          raster. This field stores the value of the zone to which the cells of
          each region in the output belong according to the connectivity rule
          defined in the number_neighbors parameter. This is the default.
          LINK         NO_LINK-Afield will not be added. The attribute table for
          the
          output raster will only contain theandfields. LINKValueCount
      excluded_value {Long}:
          A value that excludes all cells of that zone from the connectivity
          evaluation. If a cell location contains the value, no spatial
          connectivity will be evaluated, regardless of how the number of
          neighbors is specified.Cells with the excluded value will be treated
          in a similar way to
          NoData cells, and are eliminated from consideration in the operation.
          Input cells that contain the excluded value will receive 0 on the
          output raster. The excluded value is similar to the concept of a
          background value.By default, there is no value defined for this
          parameter, which means
          that all of the input cells will be considered in the operation.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output region group raster.The output is always of integer type.

        """