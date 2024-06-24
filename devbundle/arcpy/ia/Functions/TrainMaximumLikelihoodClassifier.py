# Generated documentation for module arcpy.ia.Functions


class TrainMaximumLikelihoodClassifier(object):
    """
    Generates an Esri classifier definition file (.ecd) using the Maximum Likelihood Classifier (MLC) classification definition.
    """

    @property
    def description(self) -> str:
        return """

        TrainMaximumLikelihoodClassifier_ia(in_raster, in_training_features, out_classifier_definition, {in_additional_raster}, {used_attributes;used_attributes...}, {dimension_value_field})

        Generates an Esri classifier definition file (.ecd) using the Maximum
        Likelihood Classifier (MLC) classification definition.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String):
          The raster dataset to classify.
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
          Incorporates ancillary raster datasets, such as a segmented image or
          DEM. This parameter is optional.
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
          The output JSON format file that will contain attribute information,
          statistics, hyperplane vectors, and other information for the
          classifier. An .ecd file will be created.

        """