# Generated documentation for module arcpy.sa.Functions


class PrincipalComponents(object):
    """
    Performs Principal Component Analysis (PCA) on a set of raster bands and generates a single multiband raster as output.
    """

    @property
    def description(self) -> str:
        return """

        PrincipalComponents_sa(in_raster_bands;in_raster_bands..., {number_components}, {out_data_file})

        Performs Principal Component Analysis (PCA) on a set of raster bands
        and generates a single multiband raster as output.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands.They can be integer or floating point type.
      number_components {Long}:
          Number of principal components.The number must be greater than zero
          and less than or equal to the
          total number of input raster bands.The default is the total number of
          rasters in the input.

     OUTPUTS:
      out_multiband_raster (Raster Dataset):
          The output multiband raster dataset.If all of the input bands are
          integer type, the output raster bands
          will be integer. If any of the input bands are floating point, the
          output will be floating point.If the output is an Esri Grid raster,
          the name must have less than 10
          characters.
      out_data_file {File}:
          Output ASCII data file storing principal component parameters.The
          output data file records the correlation and covariance matrices,
          the eigenvalues and eigenvectors, the percent variance each eigenvalue
          captures, and the accumulative variance described by the
          eigenvalues.The extension for the output file can be .txt or .asc.

        """