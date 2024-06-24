# Generated documentation for module arcpy.ia.Functions


class InspectTrainingSamples(object):
    """
    Estimates the accuracy of individual training samples. The cross validation accuracy is computed using the previously generated classification training result in an .ecd file and the training samples. Outputs include a raster dataset containing the misclassified class values and a training sample dataset with the accuracy score for each training sample.
    """

    @property
    def description(self) -> str:
        return """

        InspectTrainingSamples_ia(in_raster, in_training_features, in_classifier_definition, out_training_feature_class, {in_additional_raster})

        Estimates the accuracy of individual training samples. The cross
        validation accuracy is computed using the previously generated
        classification training result in an .ecd file and the training
        samples. Outputs include a raster dataset containing the misclassified
        class values and a training sample dataset with the accuracy score for
        each training sample.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String):
          The input raster to be classified.
      in_training_features (Feature Layer / Raster Catalog Layer):
          A training sample feature class created in thepane.
          Training Samples Manager
      in_classifier_definition (File):
          The .ecd output classifier file from any of the train classifier
          tools. The .ecd file is a JSON file that contains attribute
          information, statistics, or other information needed for the
          classifier.
      in_additional_raster {Mosaic Layer / Raster Layer / Image Service / String}:
          Ancillary raster datasets, such as a multispectral image or a DEM,
          will be incorporated to generate attributes and other required
          information for the classifier. This raster is necessary when
          calculating attributes such as mean or standard deviation. This
          parameter is optional.

     OUTPUTS:
      out_training_feature_class (Feature Class):
          The output individual training samples saved as a feature class. The
          associated attribute table contains an addition field listing the
          accuracy score.
      out_misclassified_raster (Raster Dataset):
          The output misclassified raster having NoData outside training
          samples. In training samples, correctly classified pixels are
          represented as NoData, and misclassified pixels are represented by
          their class value. The results is an index map of misclassified class
          values.

        """