# Generated documentation for module arcpy.management


class Append(object):
    """
    Appends to, or optionally updates, an existing target dataset with multiple input datasets. Input datasets can be feature classes, tables, shapefiles, rasters, or annotation or dimension feature classes.
    """

    @property
    def description(self) -> str:
        return """

        Append_management(inputs;inputs..., target, {schema_type}, {field_mapping}, {subtype}, {expression}, {match_fields;match_fields...}, {update_geometry})

        Appends to, or optionally updates, an existing target dataset with
        multiple input datasets. Input datasets can be feature classes,
        tables, shapefiles, rasters, or annotation or dimension feature
        classes.

     INPUTS:
      inputs (Table View / Raster Layer):
          The input datasets containing the data to be appended to the target
          dataset. Input datasets can be point, line, or polygon feature
          classes, tables, rasters, annotation feature classes, or dimensions
          feature classes.Tables and feature classes can be combined. If a
          feature class is
          appended to a table, attributes will be transferred; however, the
          features will be dropped. If a table is appended to a feature class,
          the rows from the input table will have null geometry.
      target (Table View / Raster Layer):
          The existing dataset where the data of the input datasets will be
          appended.
      schema_type {String}:
          Specifies whether the fields of the input datasets must match the
          fields of the target dataset for data to be appended.TEST-Fields of
          the input datasets must match the fields of the target
          dataset. An error will be returned if the fields do not match.
          NO_TEST-Fields of the input datasets do not need to match the
          fields of the target dataset. Fields of the input datasets that do not
          match the fields of the target dataset will not be mapped to the
          target dataset unless the mapping is explicitly set in theparameter.
          Field MapTEST_AND_SKIP-Fields of the input datasets must match the
          fields of
          the target dataset. If any of the input datasets contain fields that
          do not match the target dataset, that input dataset will be omitted
          with a warning message.
      field_mapping {Field Mappings}:
          The field map parameter controls the transfer or mapping of fields
          from the input datasets to the target dataset. It can only be used
          when the schema_type parameter is set to NO_TEST.Because the input
          datasets are appended to an existing target dataset
          with predefined fields, you cannot add, remove, reorder, or change the
          properties of the fields in the field map.The field map can be used to
          combine values from one or more input
          fields into a single output field.In Python, use the FieldMappings
          class to define this parameter.
      subtype {String}:
          The subtype description that will be assigned to all new data that is
          appended to the target dataset.
      expression {SQL Expression}:
          The SQL expression that will be used to select a subset of the input
          datasets' records. If multiple input datasets are specified, they will
          all be evaluated using the expression. If no records match the
          expression for an input dataset, no records from that dataset will be
          appended to the target dataset.For more information about SQL syntax,
          see SQL reference for query
          expressions used in ArcGIS.
      match_fields {Value Table}:
          The fields from the input datasets that will be used to match to the
          target dataset. If the values of these fields match, records from the
          input datasets will update the corresponding records of the target
          dataset.
      update_geometry {Boolean}:
          Specifies whether geometry in the target dataset will be updated with
          geometry from the input datasets if the match_fields parameter field
          values match.UPDATE_GEOMETRY-Geometry in the target dataset will be
          updated if the
          match_fields parameter field values match.NOT_UPDATE_GEOMETRY-Geometry
          will not be updated. This is the default.

        """