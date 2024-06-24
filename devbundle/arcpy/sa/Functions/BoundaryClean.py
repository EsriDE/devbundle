# Generated documentation for module arcpy.sa.Functions


class BoundaryClean(object):
    """
    Smooths the boundary between zones in a raster.
    """

    @property
    def description(self) -> str:
        return """

        BoundaryClean_sa(in_raster, {sort_type}, {number_of_runs})

        Smooths the boundary between zones in a raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster for which the boundary between zones will be
          smoothed.It must be of integer type.
      sort_type {String}:
          Specifies the type of sorting to use in the smoothing process. The
          sorting determines the priority by which cells can expand into their
          neighbors.The sorting can be based on zone value or zone
          size.NO_SORT-The priority is determined by zone value. The size of the
          zones is not considered. Zones with larger values will have a higher
          priority to expand into zones with smaller values in the smoothed
          output. This is the default.DESCEND-Zones are sorted in descending
          order by size. Zones with
          larger total areas have a higher priority to expand into zones with
          smaller total areas. This option tends to eliminate or reduce the
          prevalence of cells from smaller zones in the smoothed
          output.ASCEND-Zones are sorted in ascending order by size. Zones with
          smaller
          total areas have a higher priority to expand into zones with larger
          total areas. This option tends to preserve or increase the prevalence
          of cells from smaller zones in the smoothed output.
      number_of_runs {Boolean}:
          Specifies the number of times the smoothing process will occur, twice
          or once.TWO_WAY-The expansion and shrinking operation is performed
          twice. The
          first time, the operation is performed according to the specified sort
          type. The second time, an additional expansion and shrinking operation
          is performed with the priority reversed. This is the
          default.ONE_WAY-The expansion and shrinking operation is performed
          once
          according to the sort type.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output generalized raster.The boundaries between zones in the
          input will be smoothed.The output is always of integer type.

        """