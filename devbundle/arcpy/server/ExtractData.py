# Generated documentation for module arcpy.server


class ExtractData(object):
    """
    Extracts selected layers in the specified area of interest to a specific format and spatial reference. The extracted data is then written to a zip file.
    """

    @property
    def description(self) -> str:
        return """

        ExtractData_server(Layers_to_Clip;Layers_to_Clip..., Area_of_Interest, Feature_Format, Raster_Format, Spatial_Reference, {Custom_Spatial_Reference_Folder}, Output_Zip_File)

        Extracts selected layers in the specified area of interest to a
        specific format and spatial reference. The extracted data is then
        written to a zip file.

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
      Spatial_Reference (String):
          The spatial reference of the output data delivered by the tool.For
          standard Esri spatial references, the name you provide here should
          be the name of the desired coordinate system. This name corresponds to
          the name of the spatial reference's projection file. Alternatively,
          you can use the Well Known ID (WKID) of the coordinate system.
          For example:        Sinusoidal (world)WGS 1984 World
          MercatorNAD 1983 HARN StatePlane
          Oregon North FIPS 3601 (Meters)WGS 1984 UTM Zone 11N10200354001If you
          want the output to have the same coordinate system as the
          input, then use the string Same As Input.For any custom projection,
          the name specified should be the name of
          the custom projection file (without extension). The location of the
          custom projection files should be specified in the parameter.
      Custom_Spatial_Reference_Folder {Folder}:
          The location of any custom projection file or files referenced in the
          Spatial Reference parameter. This is only necessary if the custom
          projection file is not in the default installation Coordinate System
          folder.

     OUTPUTS:
      Output_Zip_File (File):
          The zip file that will contain the extracted data.

        """