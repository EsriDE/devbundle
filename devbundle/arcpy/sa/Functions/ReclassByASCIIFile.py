# Generated documentation for module arcpy.sa.Functions


class ReclassByASCIIFile(object):
    """
    Reclassifies (or changes) the values of the input cells of a raster using an ASCII remap file.
    """

    @property
    def description(self) -> str:
        return """

        ReclassByASCIIFile_sa(in_raster, in_remap_file, {missing_values})

        Reclassifies (or changes) the values of the input cells of a raster
        using an ASCII remap file.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      in_remap_file (File):
          ASCII remap file defining the single values or ranges to be
          reclassified and the values they will become.Allowed extensions for
          the ASCII remap files are .rmp, .txt, and .asc.
      missing_values {Boolean}:
          Denotes whether missing values in the reclass file retain their value
          or get mapped to NoData.DATA-Signifies that if any cell location on
          the input raster contains
          a value that is not present or reclassed in the remap file, the value
          should remain intact and be written for that location to the output
          raster. This is the default.NODATA-Signifies that if any cell location
          on the input raster
          contains a value that is not present or reclassed in the remap file,
          the value will be reclassed to NoData for that location on the output
          raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer
          type.

        """