# Generated documentation for module arcpy.sa.Functions


class MLClassify(object):
    """
    Performs a maximum likelihood classification on a set of raster bands and creates a classified raster as output.
    """

    @property
    def description(self) -> str:
        return """

        MLClassify_sa(in_raster_bands;in_raster_bands..., in_signature_file, {reject_fraction}, {a_priori_probabilities}, {in_a_priori_file}, {out_confidence_raster})

        Performs a maximum likelihood classification on a set of raster bands
        and creates a classified raster as output.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands.While the bands can be integer or floating
          point type, the signature
          file only allows integer class values.
      in_signature_file (File):
          The input signature file whose class signatures are used by the
          maximum likelihood classifier.A .gsg extension is required.
      reject_fraction {String}:
          Select a reject fraction, which determines whether a cell will be
          classified based on its likelihood of being correctly assigned to one
          of the classes. Cells whose likelihood of being correctly assigned to
          any of the classes is lower than the reject fraction will be given a
          value of NoData in the output classified raster.The default value is
          0.0, which means that every cell will be
          classified.Valid entries are:0.0-The rejection fraction is 0.00.005-
          The rejection fraction is
          0.0050.01-The rejection fraction is 0.010.025-The rejection fraction
          is 0.0250.05-The rejection fraction is 0.050.1-The rejection
          fraction is 0.10.25-The rejection fraction is 0.250.5-The rejection
          fraction is 0.50.75-The rejection fraction is 0.750.9-The rejection
          fraction is 0.90.95-The rejection fraction is 0.950.975-The
          rejection fraction is 0.9750.99-The rejection fraction is 0.990.995-
          The rejection fraction is 0.995
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
      out_classified_raster (Raster Dataset):
          The output classified raster.It will be of integer type.
      out_confidence_raster {Raster Dataset}:
          The output confidence raster dataset shows the certainty of the
          classification in 14 levels of confidence, with the lowest values
          representing the highest reliability. If there are no cells classified
          at a particular confidence level, that confidence level will not be
          present in the output confidence raster.It will be of integer type.

        """