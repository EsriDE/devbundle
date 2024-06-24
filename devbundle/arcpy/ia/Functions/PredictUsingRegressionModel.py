# Generated documentation for module arcpy.ia.Functions


class PredictUsingRegressionModel(object):
    """
    Predicts data values using the output from the Train Random Trees Regression Model tool.
    """

    @property
    def description(self) -> str:
        return """

        PredictUsingRegressionModel_ia(in_rasters;in_rasters..., in_regression_definition)

        Predicts data values using the output from the Train Random Trees
        Regression Model tool.

     INPUTS:
      in_rasters (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer / Image Service / String):
          The single-band, multidimensional, or multiband raster datasets, or
          mosaic datasets containing explanatory variables.
      in_regression_definition (File):
          A JSON format file that contains attribute information, statistics, or
          other information from the regression model. The file has an .ecd
          extension. The file is the output of the Train Random Trees Regression
          Model tool.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          A raster of the predicted values.

        """