# Generated documentation for module arcpy.ba


class ImportBusinessAnalystReportTemplate(object):
    """
    Imports an online report so that it can run locally using a locally installed ArcGIS Business Analyst dataset.
    """

    @property
    def description(self) -> str:
        return """

        ImportBusinessAnalystReportTemplate_ba(online_report_template_id, {output_folder}, {dataset_id}, {config})

        Imports an online report so that it can run locally using a locally
        installed ArcGIS Business Analyst dataset.

     INPUTS:
      online_report_template_id (String):
          The report template ID.
      output_folder {Folder}:
          The local folder where the report template items will be imported.
      dataset_id {String}:
          The dataset that will be used to populate the report variables.
      config {String}:
          A JSON string specifying where the report's SDCX variables
          will be stored. The config options are as follows:        id-The
          portal item ID of the SDCX.download-True or false. Set to true
          to download the SDCX, or set to
          false to reference an existing SDCX.path-The location of the SDCX. Use
          an empty string to use the existing
          default-for example, the report output folder location-or specify a
          new folder location or an existing folder that contains the
          SDCX.name-The name of the SDCX. Specify a new name for the SDCX or the
          name
          of an existing SDCX.

        """