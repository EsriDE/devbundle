# Generated documentation for module arcpy.server


class ExtractDataTask(object):
    """
    Extracts the selected layers in the specified area of interest to the selected formats and spatial reference, and returns the data in a .zip file.
    """

    @property
    def description(self) -> str:
        return """

        ExtractDataTask_server(Layers_to_Clip;Layers_to_Clip..., Area_of_Interest, Feature_Format, Raster_Format, Output_Zip_File)

        Extracts the selected layers in the specified area of interest to the
        selected formats and spatial reference, and returns the data in a .zip
        file.

     INPUTS:
      Layers_to_Clip (Layer):
          The layers to be clipped. Layers must be feature or raster; layer
          files are not supported.
      Area_of_Interest (Feature Set):
          One or more polygons by which the layers will be clipped.
      Feature_Format (String):
          Specifies the format of the output features. The format should
          be specified as follows:        Name or format - Short Name -
          extension (if any)The hyphens are required and there must be one space
          before and after
          the hyphen. For example:        File Geodatabase - GDB -
          .gdbShapefile -
          SHP - .shpAutodesk AutoCAD -
          DXF_R2007 - .dxfAutodesk AutoCAD - DWG_R2007 - .dwgBentley
          Microstation Design (V8) - DGN_V8 - .dgnThe list of short names
          supported includes DGN_V8, DWG_R14, DWG_R2000,
          DWG_R2004, DWG_R2005, DWG_R2007, DWG_R2010, DXF_R14, DXF_R2000,
          DXF_R2004, DXF_R2005, DXF_R2007, and DXF_R2010.
      Raster_Format (String):
          Specifies the format of the output raster datasets. The format
          should be specified as follows:        Name of format - Short Name -
          extension (if any)The hyphens are required and there must be one space
          before and after
          the hyphen. For example:        Esri GRID - GRIDFile
          Geodatabase - GDB -
          .gdbERDAS IMAGINE - IMG -
          .imgTagged Image File Format - TIFF - .tifPortable Network Graphics -
          PNG - .pngGraphic Interchange Format - GIF - .gifJoint Photographics
          Experts Group - JPEG - .jpgJoint Photographics Experts Group - JPEG -
          .jp2Bitmap - BMP - .bmpSome of the above raster formats have
          limitations and not all data can
          be converted to the format. For a list of formats and their
          limitations, refer to List of supported sensors.

     OUTPUTS:
      Output_Zip_File (File):
          The zip file that will contain the extracted data.

        """