# Generated documentation for module arcpy.sa.Functions


class Lookup(object):
    """
    Creates a raster by looking up values in another field in the table of the input raster.
    """

    @property
    def description(self) -> str:
        return """

        Lookup_sa(in_raster, lookup_field)

        Creates a raster by looking up values in another field in the table of
        the input raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster that contains a field from which to create a new
          raster.
      lookup_field (Field):
          Field containing the desired values for the new raster.It can be a
          numeric or string type.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster whose values are determined by the specified field
          of the input raster.

        """