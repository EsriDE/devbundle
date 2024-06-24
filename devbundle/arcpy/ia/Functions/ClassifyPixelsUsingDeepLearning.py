# Generated documentation for module arcpy.ia.Functions


class ClassifyPixelsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input raster to produce a classified raster, with each valid pixel having an assigned class label.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyPixelsUsingDeepLearning_ia(in_raster, {out_classified_raster}, in_model_definition, {arguments;arguments...}, {processing_mode}, {out_classified_folder}, {out_featureclass}, {overwrite_attachments}, {use_pixelspace})

        Runs a trained deep learning model on an input raster to produce a
        classified raster, with each valid pixel having an assigned class
        label.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer / Folder / Feature Layer / Feature Class):
          The input raster dataset that will be classified.The input can be a
          single raster, multiple rasters in a mosaic
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
      arguments {Value Table}:
          The information from the in_model_definition parameter will be used to
          set the default values for this parameter. These arguments vary,
          depending on the model architecture. The following are supported model
          arguments for models trained in ArcGIS. ArcGIS pretrained models and
          custom deep learning models may have additional arguments that the
          tool supports.batch_size-The number of image tiles processed in each
          step of the
          model inference. This depends on the memory of your graphics card. The
          argument is available for all model architectures.direction-The image
          is translated from one domain to another. Options
          are AtoB and BtoA. The argument is only available for the CycleGAN
          architecture. For more information about this argument, see How
          CycleGAN works.merge_policy-The policy for merging augmented
          predictions. Available
          options are mean, max, and min. This is only applicable when test time
          augmentation is used. The argument is available for the
          MultiTaskRoadExtractor and ConnectNet architectures. If
          IsEdgeDetection is present in the model's .emd file, the
          BDCNEdgeDetector, HEDEdgeDetector, and MMSegmentation architectures
          are also available.n_timestep-The number of time steps that will be
          used. The default is
          200. It can be increased and decreased based on the quality of
          generations. The argument is only supported for the Super Resolution
          with SR3 backbone model.padding-The number of pixels at the border of
          image tiles from which
          predictions are blended for adjacent tiles. To smooth the output while
          reducing artifacts, increase the value. The maximum value of the
          padding can be half the tile size value. The argument is available for
          all model architectures.predict_background-Specifies whether the
          background class will be
          classified. If true, the background class is also classified. The
          argument is available for UNET, PSPNET, DeepLab, MMSegmentation, and
          SAMLoRA.return_probability_raster-Specifies whether the output will be
          a
          probability raster. If true, the output will be a probability raster.
          If false, the output will be a binary classified raster. The default
          is false. If ArcGISLearnVersion is 1.8.4 or later in the model's .emd
          file, the MultiTaskRoadExtractor and ConnectNet architectures are
          available. If ArcGISLearnVersion is 1.8.4 or later and IsEdgeDetection
          is present in the model's .emd file, the BDCNEdgeDetector,
          HEDEdgeDetector, and MMSegmentation architectures are also
          available.sampling_type-The type of sampling that will be used. Two
          types of
          sampling are available: ddim and ddpm. The default is ddim, which
          generates results in fewer time steps compared to ddpm. The argument
          is only supported for the Super Resolution with SR3 backbone
          model.schedule-An optional string that sets the type of schedule. The
          default schedule is the same as the model it was trained on. The
          argument is only supported for the Super Resolution with SR3 backbone
          model.test_time_augmentation-Performs test time augmentation while
          predicting. If true, predictions of flipped and rotated variants of
          the input image will be merged into the final output. The argument is
          available for UNET, PSPNET, DeepLab, HEDEdgeDetector,
          BDCNEdgeDetector, ConnectNet, MMSegmentation, Multi-Task Road
          Extractor, and SAMLoRA.tile_size-The width and height of image tiles
          into which the imagery
          will be split for prediction. The argument is only available for the
          CycleGAN architecture.thinning-Specifies whether predicted edges will
          be thinned or
          skeletonized. Options are True and False. If IsEdgeDetection is
          present in the model's .emd file, the BDCNEdgeDetector,
          HEDEdgeDetector, and MMSegmentation architectures are
          available.threshold-The predictions that have a confidence score
          higher than
          this threshold are included in the result. The allowed values range
          from 0 to 1.0. If ArcGISLearnVersion is 1.8.4 or later in the model's
          .emd file, the MultiTaskRoadExtractor and ConnectNet architectures are
          available. If ArcGISLearnVersion is 1.8.4 or later and IsEdgeDetection
          is present in the model's .emd file, the BDCNEdgeDetector,
          HEDEdgeDetector, and MMSegmentation architectures are also available.
      processing_mode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.
      overwrite_attachments {Boolean}:
          Specifies whether existing image attachments will be
          overwritten.NO_OVERWRITE-Existing image attachments will not be
          overwritten and
          new image attachments will be stored in a new feature class. When this
          option is specified, the out_featureclass parameter must be populated.
          This is the default.OVERWRITE-The existing feature class will be
          overwritten with the new
          updated attachments.This parameter is only valid when the in_raster
          parameter value is a
          feature class with image attachments.
      use_pixelspace {Boolean}:
          Specifies whether inferencing will be performed on images in pixel
          space.NO_PIXELSPACE-Inferencing will be performed in map space. This
          is the
          default.PIXELSPACE-Inferencing will be performed in image space, and
          the
          output will be transformed back to map space. This option is useful
          when using oblique imagery or Street View imagery, where the features
          may become distorted using map space.

     OUTPUTS:
      out_classified_raster {Raster Dataset / Feature Class}:
          The name of the raster or mosaic dataset containing the result.
      out_classified_folder {Folder}:
          The folder where the output classified rasters will be stored. A
          mosaic dataset will be generated using the classified rasters in this
          folder.This parameter is required when the input raster is a folder of
          images
          or a mosaic dataset in which all items are to be processed separately.
          The default is a folder in the project folder.
      out_featureclass {Feature Class}:
          The feature class where the output classified rasters will be
          stored.This parameter is required when the input raster is a feature
          class of
          images.

        """