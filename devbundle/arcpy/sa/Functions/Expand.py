# Generated documentation for module arcpy.sa.Functions


class Expand(object):
    """
    Expands specified zones of a raster by a specified number of cells.
    """

    @property
    def description(self) -> str:
        return """

        Expand_sa(in_raster, number_cells, zone_values;zone_values..., {expand_method})

        Expands specified zones of a raster by a specified number of cells.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster for which the identified zones are to be expandedIt
          must be of integer type.
      number_cells (Long):
          The number of cells to expand each specified zone by.The value must be
          an integer greater than 1.
      zone_values (Long):
          The list of zone values to expand.The zone values must be integers.
          They can be in any order.
      expand_method {String}:
          The method used to expand the selected zones.MORPHOLOGICAL-Uses a
          mathematical morphology method to expand the
          zones. This is the default.DISTANCE-Uses a distance-based method to
          expand the zones.The DISTANCE option supports parallelization, and can
          be controlled
          with the parallelProcessingFactor environment setting.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output generalized raster.The specified zones of the input raster
          will be expanded by the
          specified number of cells.The output is always of integer type.

        """