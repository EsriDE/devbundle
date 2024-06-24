# Generated documentation for module arcpy.management


class Merge(object):
    """
    Combines multiple input datasets into a single, new output dataset. This tool can combine point, line, or polygon feature classes or tables.
    """

    @property
    def description(self) -> str:
        return """

        Merge_management(inputs;inputs..., output, {field_mappings}, {add_source})

        Combines multiple input datasets into a single, new output dataset.
        This tool can combine point, line, or polygon feature classes or
        tables.

     INPUTS:
      inputs (Table View):
          The input datasets that will be merged into a new output dataset.
          Input datasets can be point, line, or polygon feature classes or
          tables. Input feature classes must all be of the same geometry
          type.Tables and feature classes can be combined in a single output
          dataset.
          The output type is determined by the first input. If the first input
          is a feature class, the output will be a feature class. If the first
          input is a table, the output will be a table. If a table is merged
          into a feature class, the rows from the input table will have null
          geometry.
      field_mappings {Field Mappings}:
          Use the field map to reconcile schema differences and match attribute
          fields between multiple datasets. By default, the output includes all
          fields from the input datasets.Use the field map to add, delete,
          rename, and reorder fields, as well
          as change other field properties.The field map can also be used to
          combine values from two or more
          input fields into a single output field.In Python, use the
          FieldMappings class to define this parameter.
      add_source {Boolean}:
          Specifies whether source information will be added to the
          output dataset in a newtext field. The values in thefield will
          indicate the input dataset path or layer name that is the source of
          each record in the output. MERGE_SRCMERGE_SRC
          NO_SOURCE_INFO-Source information will not be added to the
          output dataset in afield. This is the default. MERGE_SRC
          ADD_SOURCE_INFO-Source information will be added to the
          output dataset in afield. MERGE_SRC

     OUTPUTS:
      output (Feature Class / Table):
          The output dataset that will contain all combined input datasets.

        """