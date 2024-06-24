# Generated documentation for module arcpy.ia.Functions


class MultidimensionalPrincipalComponents(object):
    """
    Transforms multidimensional rasters into their principal components, loadings, and eigenvalues. The tool transforms the data into a reduced number of components that account for the variance of the data, so that spatial and temporal patterns can be readily identified.
    """

    @property
    def description(self) -> str:
        return """

        MultidimensionalPrincipalComponents_ia(in_multidimensional_raster, mode, dimension, out_pc, out_loadings, {out_eigenvalues}, {variable}, {number_of_pc})

        Transforms multidimensional rasters into their principal components,
        loadings, and eigenvalues. The tool transforms the data into a reduced
        number of components that account for the variance of the data, so
        that spatial and temporal patterns can be readily identified.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster.The tool processes data along one
          dimension, such as a time series
          raster or a data cube defined by a nontime dimension [X, Y, Z]. If an
          input variable includes multiple dimensions, such as depth and time,
          the first dimension value will be used by default.You can use the Make
          Multidimensional Raster Layer tool or Subset
          Multidimensional Raster tool to redefine the multidimensional data as
          needed, such as configuring multidimensional data into a dataset with
          one dimension.
      mode (String):
          Specifies the method that will be used to perform principal component
          analysis.DIMENSION_REDUCTION-The input time series data will be
          treated as a
          set of images. Principal components that extract prevalent pattens
          over time will be computed. This is the default.SPATIAL_REDUCTION-The
          input time series data will be treated as a set
          of pixels. Principal components that extract prevalent pattens and
          locations over time will be computed as a set of one-dimensional
          arrays stored in a table.
      dimension (String):
          The dimension name used to process the principal components.
      variable {String}:
          The variable of the input multidimensional raster used in computation.
          If the input raster is multidimensional and no variable is specified,
          only the first variable will be analyzed, by default.For example, to
          find the years in which temperature values were
          highest, specify temperature as the variable to be analyzed. If you do
          not specify any variables and you have both temperature and
          precipitation variables, both variables will be analyzed, and the
          output multidimensional raster will include both variables.
      number_of_pc {String}:
          The number of principal components to compute, usually fewer than the
          number of input rasters.This parameter also takes the form of a
          percentage (%). For example, a
          value of 90% means the number of components that can explain 90
          percent of variance in the data will be computed.

     OUTPUTS:
      out_pc (Raster Dataset / Table):
          The name of the output raster dataset.When the mode parameter is
          specified as DIMENSION_REDUCTION, the
          output will be a multiband raster with the components as bands. The
          first band is the first principal component with the largest
          eigenvalue, the second band has the principal component with the
          second largest eigenvalue, and so on. The output is in CRF file format
          (.crf), which maintains the multidimensional information.When the mode
          parameter is specified as SPATIAL_REDUCTION, the output
          is a table containing a set of time series data representing the
          principal components.
      out_loadings (Raster Dataset / Table):
          The output loadings data contributing to the principal components.When
          the mode parameter is specified as DIMENSION_REDUCTION, the
          output will be a table containing the weights that each input raster
          contributed to the principal components. These weights define the
          correlations of the input data and the output principal components.
          Use the .csv file extension to output the loadings as a comma-
          separated values file.When the mode parameter is specified as
          SPATIAL_REDUCTION, the output
          is a raster where pixel values are the weights contributing the
          principal components. Pixels with larger values are more corelated to
          the principal components. This output may have a larger cell size than
          the input raster because a random reprojection is applied to reduce
          the computation complexity.
      out_eigenvalues {Table}:
          The output Eigenvalues table. Eigenvalues are values indicating the
          variance percentage of each component. Eigenvalues help you define the
          number of principal components that are needed to represent the
          dataset.

        """