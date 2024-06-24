# Generated documentation for module arcpy.conversion


class PDFToTIFF(object):
    """
    Exports a .pdf file to Tagged Image File Format (TIFF).
    """

    @property
    def description(self) -> str:
        return """

        PDFToTIFF_conversion(in_pdf_file, out_tiff_file, {pdf_password}, {pdf_page_number}, {pdf_map}, {clip_option}, {resolution}, {color_mode}, {tiff_compression}, {geotiff_tags})

        Exports a .pdf file to Tagged Image File Format (TIFF).

     INPUTS:
      in_pdf_file (File):
          The input .pdf file to be exported to TIFF.
      pdf_password {Encrypted String}:
          This parameter is unavailable at ArcGIS 3.3. It will be supported in a
          future release.
      pdf_page_number {Long}:
          The page number of the PDF document to export to TIFF.
      pdf_map {String}:
          The map that will be exported.In a .pdf file, a map is a defined
          container of graphics on the PDF
          page that has a spatial reference. A PDF map is equivalent to an
          ArcGIS Pro map in that it is the container for spatial data. A PDF
          document may have one or more maps. For example, a page may have a
          main map and an additional smaller overview or key map.If the
          geotiff_tags parameter value is specified, it will be used to
          set the output spatial reference of the .tif file.If the clip_option
          parameter value is specified, it will be used to
          define the extent of the output .tif file.You can specify the map by
          name. You can also use the LARGEST option
          to use the largest map in the PDF. This is the default.For .pdf files
          that use the OGC GeoPDF standard, the only supported
          option is LARGEST.When entering the map's name, replace any space with
          an underscore.
          For example, My Map becomes My_Map.
      clip_option {Boolean}:
          Specifies whether the entire page or only the map will be
          exported.CLIP_TO_MAP-Only the map specified in the pdf_map parameter
          will be
          exported to TIFF.NO_CLIP-The entire page will be exported to TIFF.
          This is the default.
      resolution {Long}:
          The resolution of the output .tif file in dots per inch (DPI). The
          default is 250.
      color_mode {String}:
          Specifies the number of bits that will be used to describe
          color.Additional options will be supported in a future
          release.RGB_TRUE_COLOR-32-bit RGBA color will be used. If the
          tiff_compression
          parameter is set to JPEG, 24-bit RGB color will be used. This is the
          default.
      tiff_compression {String}:
          Specifies the compression scheme for the output .tif file.LZW-Lempel-
          Ziv-Welch, a lossless data compression, will be used. This
          is the default.DEFLATE-A lossless data compression will be
          used.JPEG-JPEG lossy compression will be used. The compression quality
          will
          be automatically set to 100 and cannot be changed.NONE-Compression
          will not be applied.PACK_BITS-PackBits lossless compression will be
          used.
      geotiff_tags {Boolean}:
          Specifies whether GeoTIFF tags will be added to the output. This
          parameter is only supported if the in_pdf_file parameter value has a
          spatial reference.GEOTIFF_TAGS-GeoTIFF tags will be added to the
          output. This is the
          default.NO_GEOTIFF_TAGS-GeoTIFF tags will not be added to the output.

     OUTPUTS:
      out_tiff_file (Raster Dataset):
          The output .tif file.

        """