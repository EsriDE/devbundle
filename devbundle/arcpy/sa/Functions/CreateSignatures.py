# Generated documentation for module arcpy.sa.Functions


class CreateSignatures(object):
    """
    Creates an ASCII signature file of classes defined by input sample data and a set of raster bands.
    """

    @property
    def description(self) -> str:
        return """

        CreateSignatures_sa(in_raster_bands;in_raster_bands..., in_sample_data, out_signature_file, {compute_covariance}, {sample_field})

        Creates an ASCII signature file of classes defined by input sample
        data and a set of raster bands.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands for which to create the signatures.They can be
          integer or floating point type.
      in_sample_data (Composite Geodataset):
          The input delineating the set of class samples.The input can be an
          integer raster or a feature dataset.
      compute_covariance {Boolean}:
          Specifies whether covariance matrices in addition to the means are
          calculated.COVARIANCE-Both the covariance matrices and the means for
          all classes
          of the in_sample_data will be computed. This is the
          default.MEAN_ONLY-Only the means for all classes of the in_sample_data
          will be
          calculated.
      sample_field {Field}:
          Field of the input raster or feature sample data to assign values to
          the sampled locations (classes).Only integer or string fields are
          valid fields. The specified number
          or string will be used as the Class name in the output signature file.

     OUTPUTS:
      out_signature_file (File):
          The output signature file.A .gsg extension must be specified.

        """