# Generated documentation for module arcpy.sa.Functions


class TrainRandomTreesClassifier(object):
    """
    Generates an Esri classifier definition file (.ecd) using the Random Trees classification method.
    """

    @property
    def description(self) -> str:
        return """

        TrainRandomTreesClassifier_sa(in_raster, in_training_features, out_classifier_definition, {in_additional_raster}, {max_num_trees}, {max_tree_depth}, {max_samples_per_class}, {used_attributes;used_attributes...}, {dimension_value_field})

        Generates an Esri classifier definition file (.ecd) using the Random
        Trees classification method.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String):
          The raster dataset to classify.You can use any Esri-supported raster
          dataset. One option is a 3-band,
          8-bit segmented raster dataset in which all the pixels in the same
          segment have the same color. The input can also be a single band,
          8-bit, grayscale segmented raster.
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
      max_num_trees {Long}:
          The maximum number of trees in the forest. Increasing the number of
          trees will lead to higher accuracy rates, although this improvement
          will level off eventually. The number of trees increases the
          processing time linearly.
      max_tree_depth {Long}:
          The maximum depth of each tree in the forest. Depth is another way of
          saying the number of rules each tree is allowed to create to come to a
          decision. Trees will not grow any deeper than this setting.
      max_samples_per_class {Long}:
          The maximum number of samples that will be used to define each
          class.The default value of 1000 is recommended when the inputs are
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
          CCDC tool in the Image Analyst toolbox.

     OUTPUTS:
      out_classifier_definition (File):
          A JSON file that contains attribute information, statistics, or other
          information for the classifier. An .ecd file is created.

        """