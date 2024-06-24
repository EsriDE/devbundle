# Generated documentation for module arcpy.sa.Functions


class IsoCluster(object):
    """
    Uses an isodata clustering algorithm to determine the characteristics of the natural groupings of cells in multidimensional attribute space and stores the results in an output ASCII signature file.
    """

    @property
    def description(self) -> str:
        return """

        IsoCluster_sa(in_raster_bands;in_raster_bands..., out_signature_file, number_classes, {number_iterations}, {min_class_size}, {sample_interval})

        Uses an isodata clustering algorithm to determine the characteristics
        of the natural groupings of cells in multidimensional attribute space
        and stores the results in an output ASCII signature file.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands.They can be integer or floating point type.
      number_classes (Long):
          Number of classes into which to group the cells.
      number_iterations {Long}:
          Number of iterations of the clustering process to run.The default is
          20.
      min_class_size {Long}:
          Minimum number of cells in a valid class.The default is 20.
      sample_interval {Long}:
          The interval to be used for sampling.The default is 10.

     OUTPUTS:
      out_signature_file (File):
          The output signature file.A .gsg extension must be specified.

        """