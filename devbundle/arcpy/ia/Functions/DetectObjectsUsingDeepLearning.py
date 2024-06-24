# Generated documentation for module arcpy.ia.Functions


class DetectObjectsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input raster to produce a feature class containing the objects it finds. The features can be bounding boxes or polygons around the objects found or points at the centers of the objects.
    """

    @property
    def description(self) -> str:
        return """

        DetectObjectsUsingDeepLearning_ia(in_raster, out_detected_objects, in_model_definition, {arguments;arguments...}, {run_nms}, {confidence_score_field}, {class_value_field}, {max_overlap_ratio}, {processing_mode}, {use_pixelspace})

        Runs a trained deep learning model on an input raster to produce a
        feature class containing the objects it finds. The features can be
        bounding boxes or polygons around the objects found or points at the
        centers of the objects.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer / Folder / Feature Layer / Feature Class):
          The input image that will be used to detect objects. The input can be
          a single raster, multiple rasters in a mosaic dataset, an image
          service, a folder of images, or a feature class with image
          attachments.
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
          tool supports.padding-The number of pixels at the border of image
          tiles from which
          predictions are blended for adjacent tiles. To smooth the output while
          reducing artifacts, increase the value. The maximum value of the
          padding can be half the tile size value. The argument is available for
          all model architectures.threshold-The detections that have a
          confidence score higher than this
          threshold are included in the result. The allowed values range from 0
          to 1.0. The argument is available for all model
          architectures.batch_size-The number of image tiles processed in each
          step of the
          model inference. This depends on the memory of your graphics card. The
          argument is available for all model architectures.nms_overlap-The
          maximum overlap ratio for two overlapping features,
          which is defined as the ratio of intersection area over union area.
          The default is 0.1. The argument is available for all model
          architectures.exclude_pad_detections-If true, potentially truncated
          detections near
          the edges that are in the padded region of image chips will be
          filtered. The argument is available for SSD, RetinaNet, YOLOv3,
          DETReg, MMDetection, and Faster RCNN
          only.test_time_augmentation-Performs test time augmentation while
          predicting. If true, predictions of flipped and rotated orientations
          of the input image will be merged into the final output and their
          confidence values will be averaged. This may cause the confidence
          values to fall below the threshold for objects that are only detected
          in a few orientations (of the image). The argument is available for
          all model architectures.tile_size-The width and height of image tiles
          into which the imagery
          is split for prediction. The argument is only available for
          MaskRCNN.merge_policy-The policy for merging augmented predictions.
          Available
          options are mean, max, and min. This is only applicable when test time
          augmentation is used. The argument is only available for
          MaskRCNN.output_classified_raster-The path to the output raster. The
          argument
          is only available for MaXDeepLab.
      run_nms {Boolean}:
          Specifies whether nonmaximum suppression will be performed in which
          duplicate objects are identified and the duplicate features with lower
          confidence value are removed.NO_NMS-Nonmaximum suppression will not be
          performed. All objects that
          are detected will be in the output feature class. This is the
          default.NMS-Nonmaximum suppression will be performed and duplicate
          objects
          that are detected will be removed.
      confidence_score_field {String}:
          The name of the field in the feature class that will contain the
          confidence scores as output by the object detection method.This
          parameter is required when the run_nms parameter is set to NMS.
      class_value_field {String}:
          The name of the class value field in the input feature class.
          If a field name is not specified, aorfield will be used. If
          these fields do not exist, all records will be identified as belonging
          to one class. ClassvalueValue
      max_overlap_ratio {Double}:
          The maximum overlap ratio for two overlapping features, which is
          defined as the ratio of intersection area over union area. The default
          is 0.
      processing_mode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.
          PROCESS_CANDIDATE_ITEMS_ONLY-Only raster items with a value
          of 1 or 2 in thefield of the input mosaic dataset's attribute table
          will be processed. Candidate
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
      out_detected_objects (Feature Class):
          The output feature class that will contain geometries circling the
          object or objects detected in the input image.

        """