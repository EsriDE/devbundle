# Generated documentation for module arcpy.ra


class DetectObjectsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input raster to produce a feature class containing the objects it identifies. The feature class can be shared as a hosted feature layer in your portal. The features can be bounding boxes or polygons around the objects found, or points at the centers of the objects.
    """

    @property
    def description(self) -> str:
        return """

        DetectObjectsUsingDeepLearning_ra(inputRaster, inputModel, outputName, {modelArguments;modelArguments...}, {runNMS}, {confidenceScoreField}, {classValueField}, {maxOverlapRatio}, {processingMode})

        Runs a trained deep learning model on an input raster to produce a
        feature class containing the objects it identifies. The feature class
        can be shared as a hosted feature layer in your portal. The features
        can be bounding boxes or polygons around the objects found, or points
        at the centers of the objects.

     INPUTS:
      inputRaster (Image Service / Raster Layer / Map Server / Map Server Layer / Internet Tiled Layer / String):
          The input image used to detect objects. It can be an image service
          URL, a raster layer, an image service, a map server layer, or an
          internet tiled layer.
      inputModel (File):
          The input model can be a file or a URL of a deep learning package
          (.dlpk) item from the portal.
      outputName (String):
          The name of the output feature service of detected objects.
      modelArguments {Value Table}:
          The function model arguments are defined in the Python raster function
          class referenced by the input model. This is where you list additional
          deep learning parameters and arguments for experiments and refinement,
          such as a confidence threshold for fine tuning the sensitivity. The
          names of the arguments are populated by the tool from reading the
          Python module on the RA server.
      runNMS {Boolean}:
          Specifies whether non maximum suppression, where duplicate objects are
          identified and the duplicate feature with a lower confidence value is
          removed, will be performed.NO_NMS-All detected objects will be in the
          output feature class. This
          is the default.NMS-Duplicate detected objects will be removed.
      confidenceScoreField {String}:
          The field in the feature service that contains the confidence scores
          that will be used as output by the object detection method.This
          parameter is required when the NMS keyword is used for the runNMS
          parameter.
      classValueField {String}:
          The name of the class value field in the feature service. If a
          field name is not specified, aorfield will be used. If
          these fields do not exist, all records will be identified as belonging
          to one class. ClassvalueValue
      maxOverlapRatio {Double}:
          The maximum overlap ratio for two overlapping features, which is
          defined as the ratio of intersection area over union area. The default
          is 0.
      processingMode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.

        """