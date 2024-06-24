# Generated documentation for module arcpy.ia.Functions


class ClassifyRaster(object):
    """
    Classifies a raster dataset based on an Esri classifier definition file (.ecd) and raster dataset inputs.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyRaster_ia(in_raster, in_classifier_definition, {in_additional_raster})

        Classifies a raster dataset based on an Esri classifier definition
        file (.ecd) and raster dataset inputs.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String / Raster Dataset / Mosaic Dataset):
          The raster dataset to classify.
      in_classifier_definition (File):
          The input Esri classifier definition file (.ecd) containing the
          statistics for the chosen attributes for the classifier.
      in_additional_raster {Mosaic Layer / Raster Layer / Image Service / String / Raster Dataset / Mosaic Dataset}:
          Ancillary raster datasets, such as a multispectral image or a DEM,
          will be incorporated to generate attributes and other required
          information for the classifier. This raster is necessary when
          calculating attributes such as mean or standard deviation. This
          parameter is optional.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The path and name of the classified image you are creating.The output
          classified raster is defined by the input raster dataset
          and .ecd file inputs.

        """