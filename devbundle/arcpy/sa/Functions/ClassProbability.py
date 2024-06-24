# Generated documentation for module arcpy.sa.Functions


class ClassProbability(object):
    """
    Creates a multiband raster of probability bands, with one band being created for each class represented in the input signature file.
    """

    @property
    def description(self) -> str:
        return """

        ClassProbability_sa(in_raster_bands;in_raster_bands..., in_signature_file, {maximum_output_value}, {a_priori_probabilities}, {in_a_priori_file})

        Creates a multiband raster of probability bands, with one band being
        created for each class represented in the input signature file.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands.They can be integer or floating point type.
      in_signature_file (File):
          Input signature file whose class signatures are used to generate the a
          priori probability bands.A .gsg extension is required.
      maximum_output_value {Long}:
          Factor for scaling the range of values in the output probability
          bands.By default, the values range from 0 to 100.
      a_priori_probabilities {String}:
          Specifies how a priori probabilities will be determined.EQUAL-All
          classes will have the same a priori probability.SAMPLE-A
          priori probabilities will be proportional to the number of
          cells in each class relative to the total number of cells sampled in
          all classes in the signature file.FILE-The a priori probabilities will
          be assigned to each class from an
          input ASCII a priori probability file.
      in_a_priori_file {File}:
          A text file containing a priori probabilities for the input signature
          classes. An input for the a priori probability file is only
          required
          when theoption is used. FileThe extension for the a priori file
          can be .txt or .asc.

     OUTPUTS:
      out_multiband_raster (Raster Dataset):
          The output multiband raster dataset.It will be of integer type.If the
          output is an Esri Grid, the filename cannot have more than 9
          characters.

        """