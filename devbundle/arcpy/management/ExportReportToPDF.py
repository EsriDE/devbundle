# Generated documentation for module arcpy.management


class ExportReportToPDF(object):
    """
    Exports an ArcGIS Pro report to a PDF file.
    """

    @property
    def description(self) -> str:
        return """

        ExportReportToPDF_management(in_report, out_pdf_file, {expression}, {resolution}, {image_quality}, {embed_font}, {compress_vector_graphics}, {image_compression}, {password_protect}, {pdf_password}, {page_range_type}, {custom_page_range}, {initial_page_number}, {final_page_number})

        Exports an ArcGIS Pro report to a PDF file.

     INPUTS:
      in_report (Report / File):
          The input report or .rptx file.
      expression {SQL Expression}:
          An SQL expression used to select a subset of records. This expression
          is applied in addition to any existing expressions. For more
          information on SQL syntax, see SQL reference for query expressions
          used in ArcGIS.
      resolution {Long}:
          The resolution of the exported PDF in dots per inch (dpi).
      image_quality {String}:
          Specifies the output image quality of the PDF. The image quality
          option controls the quality of rasterized data going into the
          export.BEST-The highest available image quality. This is the
          default.BETTER-High image quality.NORMAL-A compromise between image
          quality and speed.FASTER-Lower image quality to generate the report
          faster.FASTEST-The lowest image quality to create the report the
          fastest.
      embed_font {Boolean}:
          Specifies whether fonts are embedded in the output report. Font
          embedding allows text and markers built from font glyphs to be
          displayed correctly when the PDF is viewed on a computer that does not
          have the necessary fonts installed.EMBED_FONTS-Fonts will be embedded
          in the output report. This is the
          default.NO_EMBED_FONTS-Fonts will not be embedded in the output
          report.
      compress_vector_graphics {Boolean}:
          Specifies whether to compress the vector content streams in the
          PDF.COMPRESS_GRAPHICS-Vector graphics will be compressed. This option
          should be set unless clear text is desired for troubleshooting. This
          is the default.NO_COMPRESS_GRAPHICS-Vector graphics will not be
          compressed.
      image_compression {String}:
          Specifies the compression scheme used to compress image or raster data
          in the output PDF file.NONE-Do not compress image or raster
          data.RLE-Uses Run-length encoded
          compression.DEFLATE-Uses Deflate, a lossless data compression.LZW-Uses
          Lempel-Ziv-Welch, a lossless data compression.JPEG-Uses JPEG, a lossy
          data compression.ADAPTIVE-Uses Adaptive, which automatically selects
          the best
          compression type for each image on the page. JPEG will be used for
          large images with many unique colors. Deflate will be used for all
          other images. This is the default.
      password_protect {Boolean}:
          Specifies whether password protection is needed to view the output PDF
          report.PASSWORD_PROTECT-The output PDF report document will require a
          password to open.NO_PASSWORD_PROTECT-The output PDF report document
          can be opened
          without providing a password. This is the default.
      pdf_password {Encrypted String}:
          A password to restrict opening the PDF.
      page_range_type {String}:
          Specifies the page range of the report to export.ALL-Export all pages.
          This is the default.LAST-Export the last page
          only.ODD-Export the odd numbered pages.EVEN-Export the even numbered
          pages.CUSTOM-Export a custom page range.
      custom_page_range {String}:
          The pages to be exported when the page_range_type parameter is set to
          CUSTOM. You can set individual pages, ranges, or a combination of both
          separated by commas, such as 1, 3-5, 10.
      initial_page_number {Long}:
          The initial page number of the report to create a page numbering
          offset to add additional pages to the beginning of the report.
      final_page_number {Long}:
          The page number to display on the last page of the exported PDF.

     OUTPUTS:
      out_pdf_file (File):
          The output PDF file.

        """