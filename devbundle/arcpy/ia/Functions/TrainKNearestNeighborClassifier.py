# Generated documentation for module arcpy.ia.Functions


class TrainKNearestNeighborClassifier(object):
    """
    Generates an Esri classifier definition file (.ecd) using the K-Nearest Neighbor classification method.
    """

    @property
    def description(self) -> str:
        return """

        TrainKNearestNeighborClassifier_ia(in_raster, in_training_features, out_classifier_definition, {in_additional_raster}, {kNN}, {max_samples_per_class}, {used_attributes;used_attributes...}, {dimension_value_field})

        Generates an Esri classifier definition file (.ecd) using the
        K-Nearest Neighbor classification method.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String):
          The raster dataset to classify.The single band raster or segmented
          raster, multiband raster, or a
          multidimensional raster to be classified.
      in_training_features (Feature Layer / Raster Catalog Layer):
          The training sample file or layer that delineates the training sites.
          These can be either shapefiles or feature classes that contain
          the training samples. The following field names are required in the
          training sample file:        classname-A text field indicating the
          name of the class
          categoryclassvalue-A long integer field containing the integer value
          for each
          class category
      in_additional_raster {Mosaic Layer / Raster Layer / Image Service / String}:
          Ancillary raster datasets, such as a multispectral image or a DEM,
          will be incorporated to generate attributes and other required
          information for classification. This parameter is optional.
      kNN {Long}:
          The number of neighbors that will be used in searching for each input
          pixel or segment. Increasing the number of neighbors will decrease the
          influence of individual neighbors on the outcome of the
          classification. The default value is 1.
      max_samples_per_class {Long}:
          The maximum number of training samples that will be used for each
          class. The default value of 1000 is recommended when the inputs are
          nonsegmented rasters. A value that is less than or equal to 0 means
          that the system will use all the samples from the training sites to
          train the classifier.
      used_attributes {String}:
          Specifies the attributes that will be included in the attribute table
          associated with the output raster.COLOR-The RGB color values will be
          derived from the input raster on a
          per-segment basis. This is also known as average chromaticity
          color.MEAN-The average digital number (DN) will be derived from the
          optional
          pixel image on a per-segment basis.STD-The standard deviation will be
          derived from the optional pixel
          image on a per-segment basis.COUNT-The number of pixels composing the
          segment, on a per-segment
          basis.COMPACTNESS-The degree to which a segment is compact or
          circular, on a
          per-segment basis. The values range from 0 to 1, in which 1 is a
          circle.RECTANGULARITY-The degree to which the segment is rectangular,
          on a
          per-segment basis. The values range from 0 to 1, in which 1 is a
          rectangle. This parameter is only enabled if thekey property is
          set to
          true on the input raster. If the only input to the tool is a segmented
          image, the default attributes are COLOR, COUNT, COMPACTNESS, and
          RECTANGULARITY. If an in_additional_raster value is included as an
          input with a segmented image, MEAN and STD are also available
          attributes. Segmented
      dimension_value_field {Field}:
          Contains dimension values in the input training sample feature
          class.This parameter is required to classify a time series of raster
          data
          using the change analysis raster output from the Analyze Changes Using
          CCDC tool.

     OUTPUTS:
      out_classifier_definition (File):
          A JSON formatted .ecd file that contains attribute information,
          statistics, or other information for the classifier.

        """