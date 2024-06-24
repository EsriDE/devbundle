# Generated documentation for module arcpy.ra


class Nibble(object):
    """
    Replaces cells of a raster corresponding to a mask with the values of the nearest neighbors.
    """

    @property
    def description(self) -> str:
        return """

        Nibble_ra(inputRaster, inputMaskRaster, outputName, {nibbleValues}, {nibbleNodata}, {inputZoneRaster})

        Replaces cells of a raster corresponding to a mask with the values of
        the nearest neighbors.

     INPUTS:
      inputRaster (Image Service / Raster Layer / String):
          The input raster that will be nibbled.The raster can be either integer
          or floating point type.
      inputMaskRaster (Image Service / Raster Layer / String):
          The raster used as the mask.The cells that are NoData define the cells
          that will be nibbled, or
          replaced, by the value of the closest nearest neighbour.
      outputName (String):
          The name of the output nibble raster service.The default name is based
          on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      nibbleValues {Boolean}:
          Keywords defining if NoData values in the input raster are allowed to
          nibble into the area defined by the mask raster.ALL_VALUES-Specifies
          that the nearest neighbor value will be used
          whether it is NoData or another data value in the input raster. NoData
          values in the input raster are free to nibble into areas defined in
          the mask if they are the nearest neighbor. This is the
          default.DATA_ONLY-Specifies that only data values are free to nibble
          into
          areas defined in the mask raster. NoData values in the input raster
          are not allowed to nibble into areas defined in the mask raster even
          if they are the nearest neighbor.
      nibbleNodata {Boolean}:
          Keywords defining if NoData cells in the input raster that are within
          the mask will remain NoData in the output
          raster.PRESERVE_NODATA-Specifies that NoData cells in the input raster
          and
          within the mask will remain NoData in the output. This is the
          default.PROCESS_NODATA-Specifies that NoData cells in the input raster
          and
          within the mask can be nibbled into valid output cell values.
      inputZoneRaster {Image Service / Raster Layer / String}:
          The input zone raster. For each zone, input cells that are within the
          mask will be replaced only by the nearest cell values within that same
          zone.A zone is all the cells in a raster that have the same value,
          whether
          or not they are contiguous. The input zone layer defines the shape,
          values, and locations of the zones. The zone raster can be either
          integer or floating point type.

        """