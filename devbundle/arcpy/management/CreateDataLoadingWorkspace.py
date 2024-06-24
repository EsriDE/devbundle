# Generated documentation for module arcpy.management


class CreateDataLoadingWorkspace(object):
    """
    Creates a Data Loading Workspace that can be used for data loading. The output workspace contains a collection of Microsoft Excel workbooks. These workbooks can be used to configure the source and target schema mapping.
    """

    @property
    def description(self) -> str:
        return """

        CreateDataLoadingWorkspace_management(source_target_mapping;source_target_mapping..., out_folder, {match_options;match_options...}, {mapping_table}, {calc_stats}, {match_subtypes})

        Creates a Data Loading Workspace that can be used for data loading.
        The output workspace contains a collection of Microsoft Excel
        workbooks. These workbooks can be used to configure the source and
        target schema mapping.

     INPUTS:
      source_target_mapping (Value Table):
          Defines how source data will be mapped to the target schema. Both
          workspaces and individual classes are supported as source or target
          inputs. When workspaces are used, name similarity is used to match
          objects in the source and target schema.
      out_folder (Folder):
          The output folder where the Data Loading Workspace will be created.
      match_options {String}:
          Specifies whether field names or domain value descriptions will be
          matched.MATCH_FIELDS-Field names will be matched based on similarity
          between
          the source and target fields.MATCH_VALUES-Attribute domain value
          descriptions will be matched based
          on similarity between the source and target fields. When this option
          is specified, fields will not be matched by name if the source or
          target field has a domain.
      mapping_table {Record Set}:
          A table that will be used to perform substring matching for datasets,
          values, and attribute domain coded value descriptions. Use the table
          to create matches or block them.
      calc_stats {Boolean}:
          Specifies whether the count and percentage of filled-in values will be
          calculated for fields in the source schema.CALC_STATS-The count and
          percentage of filled-in values will be
          calculated.NO_STATS-No calculations will be performed on the field
          values. This
          is the default.
      match_subtypes {Boolean}:
          Specifies whether separate Data Mapping workbooks will be created by
          subtype if they exist.MATCH_SUBTYPES-Separate Data Mapping workbooks
          will be created for
          each match if they exist. The class name will not be used to match
          candidates if subtypes exist. This is the
          default.NO_MATCH_SUBTYPES-Dataset matching will only be attempted at
          the class
          level. If classes contain subtypes, a subtype sheet will be created in
          the Data Mapping workbook.

        """