# Generated documentation for module arcpy.sa.Functions


class IsoClusterUnsupervisedClassification(object):
    """
    Performs unsupervised classification on a series of input raster bands using the Iso Cluster and Maximum Likelihood Classification tools.
    """

    @property
    def description(self) -> str:
        return """

        IsoClusterUnsupervisedClassification_sa(in_raster_bands, Number_of_classes, {Minimum_class_size}, {Sample_interval}, {out_signature_file})

        Performs unsupervised classification on a series of input raster bands
        using the Iso Cluster and Maximum Likelihood Classification tools.

     INPUTS:
      in_raster_bands (Raster Layer / Mosaic Layer):
          The input raster bands.They can be integer or floating point type.
      Number_of_classes (Long):
          Number of classes into which to group the cells.
      Minimum_class_size {Long}:
          Minimum number of cells in a valid class.The default is 20.
      Sample_interval {Long}:
          The interval to be used for sampling.The default is 10.

     OUTPUTS:
      Output_classified_raster (Raster Dataset):
          The output classified raster.
      out_signature_file {File}:
          The output signature file.A .gsg extension must be specified.

        """