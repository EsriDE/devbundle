# Generated documentation for module arcpy.sa.Functions


class Nibble(object):
    """
    Replaces cells of a raster corresponding to a mask with the value of the nearest neighbor.
    """

    @property
    def description(self) -> str:
        return """

        Nibble_sa(in_raster, in_mask_raster, {nibble_values}, {nibble_nodata}, {in_zone_raster})

        Replaces cells of a raster corresponding to a mask with the value of
        the nearest neighbor.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster with the masked locations that will be replaced by
          the value of their nearest neighbor.The input raster can be either
          integer or floating point type.
      in_mask_raster (Composite Geodataset):
          The raster that identifies the locations in the input raster that will
          be replaced.Cells with a value of NoData are considered to be within
          the masked
          area. In the output raster, these locations will be replaced by the
          value of their nearest neighbor in the in_raster value.The mask raster
          can be either integer or floating point type.
      nibble_values {Boolean}:
          Specifies whether NoData cells in the input raster can replace cells
          in the masked areas if they are the nearest neighbor.ALL_VALUES-Both
          NoData and data values can replace cells in the masked
          area. This means that NoData values in the input raster can replace
          areas defined in the mask if they are the nearest neighbor. This is
          the default.DATA_ONLY-Only data values can replace cells in the masked
          area.
          NoData values in the input raster cannot replace areas defined in the
          mask raster even if they are the nearest neighbor.
      nibble_nodata {Boolean}:
          Specifies whether NoData cells in the input raster that are within the
          masked area will be preserved or replaced.PRESERVE_NODATA-Any NoData
          cells in the input raster that are within
          the masked area will be preserved (remain as NoData) in the output.
          This is the default.PROCESS_NODATA-NoData cells in the input raster
          that are within the
          masked area can be replaced with the value of the nearest neighbor
          that is outside the masked area.
      in_zone_raster {Composite Geodataset}:
          The input zone raster. For each zone, input cells that are within the
          mask will be replaced only by the nearest cell values within that same
          zone.A zone is all the cells in a raster that have the same value,
          whether
          or not they are contiguous. The input zone layer defines the shape,
          values, and locations of the zones. The zone raster can be either
          integer or floating point type.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster with the replaced cells.The identified input cells
          will be replaced with the values of their
          nearest neighbor.If the in_raster value is integer, the output raster
          will be integer.
          If it is floating point, the output will be floating point.

        """