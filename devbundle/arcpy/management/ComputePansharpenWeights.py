# Generated documentation for module arcpy.management


class ComputePansharpenWeights(object):
    """
    Calculates an optimal set of pan sharpened weights for new or custom sensor data.
    """

    @property
    def description(self) -> str:
        return """

        ComputePansharpenWeights_management(in_raster, in_panchromatic_image, {band_indexes})

        Calculates an optimal set of pan sharpened weights for new or custom
        sensor data.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          A multispectral raster that has a panchromatic band.
      in_panchromatic_image (Raster Layer):
          The panchromatic band associated with the multispectral raster.
      band_indexes {String}:
          The band order for the pan sharpened weights.If a raster product is
          used as the in_raster parameter, the band order
          within the raster product template will be used.

        """