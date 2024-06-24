# Generated documentation for module arcpy.ia.Functions


class ClassifyRasterUsingSpectra(object):
    """
    Classifies a multiband raster dataset using spectral matching techniques. The input spectral data can be provided as a point feature class or a .json file.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyRasterUsingSpectra_ia(in_raster, in_spectra_file, {method}, {thresholds}, {out_score_raster}, {out_classifier_definition})

        Classifies a multiband raster dataset using spectral matching
        techniques. The input spectral data can be provided as a point feature
        class or a .json file.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String / Raster Dataset / Mosaic Dataset):
          The input multiband raster.
      in_spectra_file (Feature Layer / File / String):
          The spectral information for different pixel classes. The
          spectral information can be provided as point features, a
          training sample point feature class generated from thepane, or a .json
          file that contains the class spectral profiles. Training
          Samples Manager
      method {String}:
          Specifies the spectral matching method that will be used.SAM-The
          vector angle between the input multiband raster and the
          reference spectra will be calculated in which the spectra of each
          pixel is treated as a vector. Angle values are in radians.SID-The
          spectral information divergence between the input multiband
          raster and the reference spectra will be calculated. A score will be
          calculated for each pixel based on the divergence between the
          probability distributions of the pixel and reference spectra. Values
          are in radians.
      thresholds {String}:
          The threshold for spectral matching. Pixel values that exceed this
          value will be classified as undefined. This can be a single value
          applied to all spectral classes or a space-delimited list of values
          for each class.

     OUTPUTS:
      out_classified_raster (Raster Dataset):
          The output classified raster.
      out_score_raster {Raster Dataset}:
          A multiband raster that stores the matching results for each end
          member. The band order follows the order of the classes in the
          in_spectra_file parameter value. If the input is a multidimensional
          raster, the output format must be CRF.
      out_classifier_definition {File}:
          The output .ecd file.

        """