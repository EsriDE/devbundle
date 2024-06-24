# Generated documentation for module arcpy.td


class GenerateTerritoryReport(object):
    """
    Creates a summary report of a territory solution or a comparison report of two solutions.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTerritoryReport_td(in_territory_solution, level, {report_type}, {report_folder}, {report_title}, {report_format;report_format...}, {comparison_territory_solution}, {comparison_level})

        Creates a summary report of a territory solution or a comparison
        report of two solutions.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The input territory solution for the report.
      level (String):
          Specifies the territory level that will be used to create the
          report.ALL_LEVELS-All territory levels will appear in the report.
      report_type {String}:
          Specifies the type of report that will be
          generated.TERRITORY_SUMMARY-The report will contain a summary of a
          territory
          solution, such as hierarchy and statistics. This is the
          default.COMPARE_TERRITORIES-The report will compare two territory
          solutions.REALIGNMENT-The report will contain a summary realignment
          report for
          the territories.REALIGNMENT_DETAILED-The report will contain a list
          of the reassigned
          features.
      report_folder {Folder}:
          The output location where the report will be saved.
      report_title {String}:
          The title of the report.
      report_format {String}:
          Specifies the format of the output report.PDF-The report will be in
          PDF format. This is the default.XLSX-The
          report will be in XLSX format.HTML-The report will be in HTML
          format.ZIP-The report will be in ZIP format.CSV-The report will be in
          CSV format.
      comparison_territory_solution {Group Layer / Feature Dataset / String}:
          The territory solution for the comparison report.
      comparison_level {String}:
          Specifies the territory level that will be used for the comparison or
          realignment report.ALL_LEVELS-All territory levels will be used for
          the comparison or
          realignment report.

        """