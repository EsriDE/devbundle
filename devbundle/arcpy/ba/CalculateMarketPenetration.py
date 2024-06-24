# Generated documentation for module arcpy.ba


class CalculateMarketPenetration(object):
    """
    Calculates the market penetration based on the number of customers within an area compared to a demographic variable such as total population.
    """

    @property
    def description(self) -> str:
        return """

        CalculateMarketPenetration_ba(in_features, out_feature_class, id_field, market_penetration_base_field, in_customer_features, {area_description_field}, {weight_field}, {create_report}, {store_id}, {link_field}, {report_title}, {report_folder}, {report_format;report_format...})

        Calculates the market penetration based on the number of customers
        within an area compared to a demographic variable such as total
        population.

     INPUTS:
      in_features (Feature Layer):
          The input feature class used for calculating market penetration.
      id_field (Field):
          A unique ID field in the market penetration layer.
      market_penetration_base_field (Field):
          The field containing the values used to calculate market
          penetration. This field will be used as the denominator and represents
          your market-for example,or. Total PopulationTotal Households
      in_customer_features (Feature Layer):
          The input feature class containing the points for the customer layer.
      area_description_field {Field}:
          The field used to describe each feature in the market penetration
          layer.
      weight_field {Field}:
          The field in the customer layer used as a weight to calculate market
          penetration rather than customer counts.
      create_report {Boolean}:
          Specifies whether a summary report will be created per boundary or by
          combining reports into a single report file.CREATE_REPORT-A summary
          report will be created.DO_NOT_CREATE_REPORT-A
          summary report will not be created. This is the
          default.
      store_id {Field}:
          A unique identifier associated with each store for each trade area.
      link_field {Field}:
          An ID that assigns a trade area to a customer.
      report_title {String}:
          The title of the report.
      report_folder {Folder}:
          The output directory that will contain the report.
      report_format {String}:
          Specifies one or more output report formats. The default value is PDF.
          Additional available formats: XLSX, HTML, CSV, PAGX.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that contains the calculated market
          penetration features.

        """