# Generated documentation for module arcpy.management


class GetCellValue(object):
    """
    Retrieves the value of a given pixel using its x, y coordinates.
    """

    @property
    def description(self) -> str:
        return """

        GetCellValue_management(in_raster, location_point, {band_index;band_index...})

        Retrieves the value of a given pixel using its x, y coordinates.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Layer):
          The raster that you want to query.
      location_point (Point):
          The X and Y coordinates of the pixel location.
      band_index {Value Table}:
          Specify the bands that you want to query. Leave blank to query all
          bands in a multiband dataset.

        """