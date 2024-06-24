# Generated documentation for module arcpy.management


class GenerateBlockAdjustmentReport(object):
    """
    Generates a report after performing an ortho mapping block adjustment on a mosaic dataset. The report is useful when evaluating the quality and accuracy of the ortho mapping products.
    """

    @property
    def description(self) -> str:
        return """

        GenerateBlockAdjustmentReport_management(input_mosaic_dataset, input_solution_table, input_solution_point, output_report, {input_control_point_for_adjustment}, {report_format})

        Generates a report after performing an ortho mapping block adjustment
        on a mosaic dataset. The report is useful when evaluating the quality
        and accuracy of the ortho mapping products.

     INPUTS:
      input_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset path.
      input_solution_table (Table View):
          The associated solution point table after block adjustment.
      input_solution_point (Table View):
          The solution point feature class.
      input_control_point_for_adjustment {Table View}:
          The associated control points table, which may include tie points and
          ground control points.
      report_format {String}:
          Specifies the output format of the block adjustment report.HTML-The
          adjustment report will be created in HTML format. This is the
          default.PDF-The adjustment report will be created in PDF
          format.JSON-The adjustment report will be created in JSON format.BRIEF
          JSON-The adjustment report will be created in an abbreviated
          JSON format.

     OUTPUTS:
      output_report (File):
          The output ortho mapping report file path and name. The supported
          output format for a website is HTML.

        """