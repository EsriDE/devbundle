# Generated documentation for module arcpy.sa.Functions


class Shrink(object):
    """
    Shrinks the selected zones by a specified number of cells by replacing them with the value of the cell that is most frequent in its neighborhood.
    """

    @property
    def description(self) -> str:
        return """

        Shrink_sa(in_raster, number_cells, zone_values;zone_values..., {shrink_method})

        Shrinks the selected zones by a specified number of cells by replacing
        them with the value of the cell that is most frequent in its
        neighborhood.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster for which the identified zones are to be shrunk.It
          must be of integer type.
      number_cells (Long):
          The number of cells by which to shrink each specified zone.The value
          must be an integer greater than 0.
      zone_values (Long):
          The list of zone values to shrink.The zone values must be integers.
          They can be in any order.
      shrink_method {String}:
          The method to use to shrink the selected zones.MORPHOLOGICAL-Uses a
          mathematical morphology method to shrink the
          zones. This is the default.DISTANCE-Uses a distance-based method to
          shrink the zones.The DISTANCE option supports parallelization, and can
          be controlled
          with the parallelProcessingFactor environment setting.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output generalized raster.The specified zones of the input raster
          will be shrunk by the
          specified number of cells.The output is always of integer type.

        """