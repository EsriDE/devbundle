# Generated documentation for module arcpy.sa.Functions


class Reclassify(object):
    """
    Reclassifies (or changes) the values in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Reclassify_sa(in_raster, reclass_field, remap, {missing_values})

        Reclassifies (or changes) the values in a raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      reclass_field (Field):
          Field denoting the values that will be reclassified.
      remap (Remap):
          The Remap object is used to specify how to reclassify values of the
          input raster.There are two ways to define how the values will be
          reclassified in
          the output raster: RemapRange and RemapValue. Either ranges of input
          values can be assigned to a new output value, or individual values can
          be assigned to a new output value.The following are the forms of the
          remap objects.RemapRange (remapTable)RemapValue (remapTable)
      missing_values {Boolean}:
          Denotes whether missing values in the reclass table retain their value
          or get mapped to NoData.DATA-Signifies that if any cell location on
          the input raster contains
          a value that is not present or reclassed in a remap table, the value
          should remain intact and be written for that location to the output
          raster. This is the default.NODATA-Signifies that if any cell location
          on the input raster
          contains a value that is not present or reclassed in a remap table,
          the value will be reclassed to NoData for that location on the output
          raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer
          type.

        """