# Generated documentation for module arcpy.indoors


class UpgradeIndoorsDatabase(object):
    """
    Upgrades an existing Indoors workspace by creating or updating schema items to conform to the latest ArcGIS Indoors Information Model schema.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeIndoorsDatabase_indoors(in_workspace, {upgrade_attribute_rules}, {upgrade_indoors_database})

        Upgrades an existing Indoors workspace by creating or updating schema
        items to conform to the latest ArcGIS Indoors Information Model
        schema.

     INPUTS:
      in_workspace (Workspace):
          The existing geodatabase that contains Indoors model schema items
          created by the Create Indoors Database or Create Indoors Dataset
          tools. This parameter accepts a file geodatabase or an enterprise
          geodatabase.
      upgrade_attribute_rules {Boolean}:
          Specifies whether validation attribute rules will be created or
          updated for use in Indoors quality control workflows. If the input
          Indoors database is an enterprise geodatabase, branch versioning must
          be enabled.UPGRADE_ATTRIBUTE_RULES-Validation attribute rules will be
          created or
          updated if there are existing Indoors attribute rules in the input
          database. This is the default.NO_UPGRADE_ATTRIBUTE_RULES-Validation
          attribute rules will not be
          created or updated.
      upgrade_indoors_database {String}:
          Specifies whether the input Indoors database will be upgraded with
          schema changes or a report will be generated with potential schema
          changes that will be made to the input Indoors
          database.UPGRADE_DATABASE-The input Indoors database will be upgraded.
          This is
          the default.GENERATE_REPORT-A text file report will be generated with
          a list of
          schema changes that will be made to the input Indoors database during
          the upgrade process and any issues that would result in the schema not
          being updated. The input Indoors database will not be upgraded.

        """