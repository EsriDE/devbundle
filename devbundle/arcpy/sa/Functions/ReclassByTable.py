# Generated documentation for module arcpy.sa.Functions


class ReclassByTable(object):
    """
    Reclassifies (or changes) the values of the input cells of a raster using a remap table.
    """

    @property
    def description(self) -> str:
        return """

        ReclassByTable_sa(in_raster, in_remap_table, from_value_field, to_value_field, output_value_field, {missing_values})

        Reclassifies (or changes) the values of the input cells of a raster
        using a remap table.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      in_remap_table (Table View):
          Table holding fields defining value ranges to be reclassified and the
          values they will become.
      from_value_field (Field):
          Field holding the beginning value for each value range to be
          reclassified.This is a numeric field of the input remap table.
      to_value_field (Field):
          Field holding the ending value for each value range to be
          reclassified.This is a numeric field of the input remap table.
      output_value_field (Field):
          Field holding the integer values to which each range should be
          changed.This is an integer field of the input remap table.
      missing_values {Boolean}:
          Denotes whether missing values in the reclass table retain their value
          or get mapped to NoData.DATA-Signifies that if any cell location on
          the input raster contains
          a value not present or reclassed in a remap table, the value should
          remain intact and be written for that location to the output raster.
          This is the default.NODATA-Signifies that if any cell location on the
          input raster
          contains a value not present or reclassed in a remap table, the value
          will be reclassed to NoData for that location on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer
          type.

        """