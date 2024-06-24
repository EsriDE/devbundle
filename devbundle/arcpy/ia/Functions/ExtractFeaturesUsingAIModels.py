# Generated documentation for module arcpy.ia.Functions


class ExtractFeaturesUsingAIModels(object):
    """
    Runs one or more pretrained deep learning models on an input raster to extract features and automate the postprocessing of the inferenced outputs.
    """

    @property
    def description(self) -> str:
        return """

        ExtractFeaturesUsingAIModels_ia(in_raster, mode, out_location, out_prefix, {area_of_interest}, {pretrained_models;pretrained_models...}, {additional_models;additional_models...}, {confidence_threshold}, {save_intermediate_output}, {test_time_augmentation}, {buffer_distance}, {extend_length}, {smoothing_tolerance}, {dangle_length}, {in_road_features}, {road_buffer_width}, {regularize_parcels}, {post_processing_workflow}, {out_features}, {parcel_tolerance}, {regularization_method}, {poly_tolerance}, {prompt}, {in_features}, {out_summary})

        Runs one or more pretrained deep learning models on an input raster to
        extract features and automate the postprocessing of the inferenced
        outputs.

     INPUTS:
      in_raster (Raster Layer / Raster Dataset / Mosaic Layer):
          The input raster on which processing will be performed.If the mode
          parameter is specified as Only Postprocess, a raster with
          binary classification is required for this parameter.
      mode (String):
          Specifies the mode that will be used for the processing of the input
          raster.Infer and Postprocess-Features will be extracted from the
          imagery and
          postprocessed. This is the default.Only Postprocess-The input raster
          will be directly postprocessed. A
          single band raster with binary classification is required for this
          option.
      out_location (Workspace):
          The file geodatabase where the intermediate output from the models and
          the final postprocessed output will be stored.
      out_prefix (String):
          A prefix that will be added to the name of the outputs that will be
          saved to the output location. The prefix will also be used as the name
          of a group layer that will be used to display all outputs.
      area_of_interest {Feature Set}:
          The geographical extent that will be used to extract features. Only
          features within the area of interest will be extracted.
      pretrained_models {String}:
          The ArcGIS pretrained models from ArcGIS Living Atlas of the World
          that can be used on the provided input raster. This parameter requires
          an internet connection to download the pretrained models.
      additional_models {Value Table}:
          The deep learning models that can be used on the provided input raster
          and the postprocessing workflow that will be used for additional model
          files (.dlpk and .emd). Available postprocessing workflows are as
          follows:Line Regularization-The postprocessing workflow will extract
          line
          features from a single band raster with binary classification and
          generate a polyline feature class after refining it. This workflow
          also supports deep learning models that generate polyline feature
          classes.Parcel Regularization-The postprocessing workflow will extract
          parcels
          from a single band raster with binary classification and generate a
          polygon feature class after refining it.Polygon Regularization-The
          postprocessing workflow will generate a
          polygon feature class after refining it. This workflow is only
          compatible with object detection models.Polygon Segmentation-The
          postprocessing workflow will generate a
          polygon feature class containing the detected objects using their
          centroid or bounding box. The segmentation method is specified using
          the prompt parameter.None-No postprocessing workflow will be applied.
          This is the default.
      confidence_threshold {Double}:
          The minimum confidence of deep learning model that will be used when
          detecting objects. The value must be between 0 and 1.
      save_intermediate_output {Boolean}:
          Specifies whether the intermediate outputs will be saved to the output
          location. The term intermediate outputs refers to the results
          generated after the model has been inferenced.TRUE-The intermediate
          outputs will be saved to the output
          location.FALSE-The intermediate outputs will not be saved. This is the
          default.
      test_time_augmentation {Boolean}:
          Specifies whether predictions of flipped and rotated variants of the
          input image will be merged into the final output.TRUE-Predictions of
          flipped and rotated variants of the input image
          will be merged into the final output.FALSE-Predictions of flipped and
          rotated variants of the input image
          will not be merged into the final output. This is the default.
      buffer_distance {Linear Unit}:
          The distance that will be used to buffer polyline features before they
          are used in postprocessing. The default is 15 meters.
      extend_length {Linear Unit}:
          The maximum distance a line segment will be extended to an
          intersecting feature. The default is 25 meters.
      smoothing_tolerance {Linear Unit}:
          The tolerance used by the Polynomial Approximation with Exponential
          Kernel (PAEK) algorithm. The default is 30 meters.
      dangle_length {Linear Unit}:
          The length at which line segments that do not touch another line at
          both endpoints (dangles) will be trimmed. The default is 5 meters.
      in_road_features {Feature Layer / Feature Class}:
          A road feature class that will be used for refining the parcels. The
          input can be a polygon or polyline feature class.
      road_buffer_width {Linear Unit}:
          The buffer distance that will be used for the input road features. The
          default value is 5 meters for polyline features and 0 meters for
          polygon features.
      regularize_parcels {Boolean}:
          Specifies whether extracted parcels will be normalized by eliminating
          undesirable artifacts in their geometry.TRUE-Extracted parcels will be
          normalized. This is the
          default.FALSE-Extracted parcels will not be normalized.
      post_processing_workflow {String}:
          Specifies the postprocessing workflow that will be used.Line
          Regularization-Line features will be extracted from a single band
          raster with binary classification and a polyline feature class will be
          generated after refining it.Parcel Regularization-Parcels will be
          extracted from a single band
          raster with binary classification and a polygon feature class will be
          generated after refining it.Polygon Regularization-A polygon feature
          class will be generated
          after refining it. This workflow is only compatible with object
          detection models.
      parcel_tolerance {Linear Unit}:
          The minimum distance between coordinates before they are considered
          equal. This parameter is used to reduce slivers between extracted
          parcels. The default is 3 meters.
      regularization_method {String}:
          Specifies the regularization method that will be used in
          postprocessing.Right Angles-Shapes composed of 90° angles between
          adjoining edges
          will be constructed. This is the default.Right Angles and
          Diagonals-Shapes composed of 45° and 90° angles
          between adjoining edges will be constructed.Any Angles-Shapes that
          form any angles between adjoining edges will be
          constructed.Circle-The maximum distance from the boundary of the
          feature being
          processed will be used.
      poly_tolerance {Linear Unit}:
          The maximum distance that the regularized footprint can deviate from
          the boundary of its originating feature. The default is 1 meter.
      prompt {String}:
          Specifies the segmentation method that will be used when the
          additional_models parameter is set to Polygon Segmentation.Centroid-
          The centroid of the detections will be used to indicate to
          the polygon segmentation model what to segment in the input
          raster.Bounding Box-The bounding box of the detections will be used
          to
          indicate to the polygon segmentation model what to segment in the
          input raster.None-No segmentation method will be used. This is the
          default
      in_features {Feature Layer / Feature Class}:
          The feature class on which postprocessing will be performed. This
          parameter is only supported when the post_processing_workflow
          parameter is set to Line Regularization or Polygon Regularization.

     OUTPUTS:
      out_features {Feature Class}:
          The feature class containing the postprocessed output.
      out_summary {Table}:
          The table that will contain a list of outputs that were generated
          along with their respective paths.

        """