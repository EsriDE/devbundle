# Generated documentation for module arcpy.topographic


class ImportGeneralizationData(object):
    """
    Imports data from a production schema to a themed generalization database using generalization rules defined in a Microsoft Excel spreadsheet.
    """

    @property
    def description(self) -> str:
        return """

        ImportGeneralizationData_topographic(input_geodatabase, target_geodatabase, rule_file, data_theme)

        Imports data from a production schema to a themed generalization
        database using generalization rules defined in a Microsoft Excel
        spreadsheet.

     INPUTS:
      input_geodatabase (Workspace):
          The geodatabase containing data in a production schema.
      target_geodatabase (Workspace):
          The target geodatabase where the data optimized for generalization
          will be loaded.
      rule_file (File):
          The Excel file containing the generalization rules. This file defines
          features participating in the generalization process and determines
          the data that will be loaded and how it is organized. An example rule
          file is provided in the product file downloads for Defense Mapping and
          Production Mapping.
      data_theme (String):
          A theme that specifies the type of data to be generalized.
          Available themes are automatically populated from theparameter. The
          values provided in the example rule file are as follows:
          Generalization Rule FileTRANS-A data theme that groups features in a
          transportation network
          such as roads and railways.STRUCTURE-A data theme that groups
          structural features such as
          buildings.HYDRO-A data theme that groups water features such as lakes
          and
          rivers.SOE-A skin of the earth data theme that groups polygon features
          that
          cover the entire surface of the earth with no holes or gaps. It can
          consist of water, vegetation, land, and artificial features.GENERAL-A
          data theme that groups features other than those defined by
          another theme.

        """