# Generated documentation for module arcpy.ba


class MeasureCannibalization(object):
    """
    Calculates the amount of overlap between two or more polygons. Overlap refers to the extent of the polygons beyond intersection.
    """

    @property
    def description(self) -> str:
        return """

        MeasureCannibalization_ba(in_features, area_id_field, area_description_field, out_feature_class, {store_id_field}, {create_report}, {report_title}, {report_folder}, {report_format;report_format...}, {variables;variables...})

        Calculates the amount of overlap between two or more polygons. Overlap
        refers to the extent of the polygons beyond intersection.

     INPUTS:
      in_features (Feature Layer):
          The input polygon features that will be analyzed for overlap.
      area_id_field (Field):
          The field that uniquely identifies each feature in the input layer.
      area_description_field (Field):
          The field that describes each feature in the input layer.
      store_id_field {Field}:
          The unique ID that associates a store with each polygon when the
          inputs are trade areas.
      create_report {Boolean}:
          Specifies whether a report will be generated.CREATE_REPORT-A report
          will be generated.DO_NOT_CREATE_REPORT-A report
          will not be generated. This is the
          default.
      report_title {String}:
          The title of the report. The default value is Measure Cannibalization.
      report_folder {Folder}:
          The output location where the report will be saved.
      report_format {String}:
          The output format or formats of the report.
      variables {String}:
          One or more variables that will be used to calculate additional
          overlap metrics-for example, the total number of people and households
          in intersection areas, or the percentage of the total number of people
          and households in a trade area falling into overlapped area.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will contain the areas of overlap found
          in the input layer.

        """