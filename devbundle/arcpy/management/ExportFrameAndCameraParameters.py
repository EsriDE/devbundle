# Generated documentation for module arcpy.management


class ExportFrameAndCameraParameters(object):
    """
    Exports frame and camera parameters from a mosaic dataset that contains frame imagery.
    """

    @property
    def description(self) -> str:
        return """

        ExportFrameAndCameraParameters_management(input_mosaic_dataset, output_file, {output_format})

        Exports frame and camera parameters from a mosaic dataset that
        contains frame imagery.

     INPUTS:
      input_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset.
      output_format {String}:
          Specifies the output file format for the frame and camera
          parameters.ESRI_FRAME_AND_CAMERA_TABLE-The frame and camera parameters
          will be
          exported as an Esri Frames and Camera table (.csv file). This is the
          default.PIX4D_CALIBRATED_CAMERA_PARAMETERS-The frame and camera
          parameters
          will be exported using the Pix4D calibrated camera parameters format
          (.txt file).

     OUTPUTS:
      output_file (File):
          The output file containing the frame and camera parameters. Supported
          file formats include .csv and .txt.

        """