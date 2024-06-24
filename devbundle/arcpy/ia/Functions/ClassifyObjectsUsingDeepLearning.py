# Generated documentation for module arcpy.ia.Functions


class ClassifyObjectsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input raster and an optional feature class to produce a feature class or table in which each input object or feature has an assigned class or category label.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyObjectsUsingDeepLearning_ia(in_raster, out_feature_class, in_model_definition, {in_features}, {class_label_field}, {processing_mode}, {model_arguments;model_arguments...}, {caption_field})

        Runs a trained deep learning model on an input raster and an optional
        feature class to produce a feature class or table in which each input
        object or feature has an assigned class or category label.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer / Folder / Feature Layer / Feature Class):
          The input image that will be used to classify objects.The input can be
          a single raster, multiple rasters in a mosaic
          dataset, an image service, a folder of images, or a feature class with
          image attachments.
      in_model_definition (File / String):
          The in_model_definition parameter value can be an Esri model
          definition JSON file (.emd), a JSON string, or a deep learning model
          package (.dlpk). A JSON string is useful when this tool is used on the
          server so you can paste the JSON string rather than upload the .emd
          file. The .dlpk file must be stored locally.It contains the path to
          the deep learning binary model file, the path
          to the Python raster function to be used, and other parameters such as
          preferred tile size or padding.
      in_features {Feature Class / Feature Layer}:
          The point, line, or polygon input feature class that identifies the
          location of each object or feature to be classified and labelled. Each
          row in the input feature class represents a single object or
          feature.If no input feature class is provided, it is assumed that each
          input
          image contains a single object to be classified. If the input image or
          images use a spatial reference, the output from the tool is a feature
          class in which the extent of each image is used as the bounding
          geometry for each labelled feature class. If the input image or images
          are not spatially referenced, the output from the tool is a table
          containing the image ID values and the class labels for each image.
      class_label_field {String}:
          The name of the field that will contain the class or category label in
          the output feature class. If no field name is provided, afield
          will be generated in the
          output feature class. ClassLabel
      processing_mode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.
      model_arguments {Value Table}:
          The information from the in_model_definition parameter will be used to
          set the default values for this parameter. These arguments vary,
          depending on the model architecture. The following are supported model
          arguments for models trained in ArcGIS. ArcGIS pretrained models and
          custom deep learning models may have additional arguments that the
          tool supports.batch_size-The number of image tiles processed in each
          step of the
          model inference. This depends on the memory of your graphic card. The
          argument is available for all model
          architectures.test_time_augmentation-Performs test time augmentation
          while
          predicting. If true, predictions of flipped and rotated variants of
          the input image will be merged into the final output. The argument is
          available for all model architectures.score_threshold-The predictions
          above this confidence score are
          included in the result. The allowed values range from 0 to 1.0. The
          argument is available for all model architectures.
      caption_field {String}:
          The name of the field that will contain the text or caption in the
          output feature class. This parameter is only supported when an Image
          Captioner model is used. If no field name is specified, afield
          will be generated in the
          output feature class. Caption

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will contain geometries surrounding the
          objects or feature from the input feature class, as well as a field to
          store the categorization label.

        """