# Generated documentation for module arcpy.management


class ApplySymbologyFromLayer(object):
    """
    Applies the symbology from a specified layer or layer file to the input. It can be applied to feature, raster, network analysis, TIN, and geostatistical layers.
    """

    @property
    def description(self) -> str:
        return """

        ApplySymbologyFromLayer_management(in_layer, in_symbology_layer, {symbology_fields;symbology_fields...}, {update_symbology})

        Applies the symbology from a specified layer or layer file to the
        input. It can be applied to feature, raster, network analysis, TIN,
        and geostatistical layers.

     INPUTS:
      in_layer (Feature Layer / Raster Layer / Layer):
          The layer to which the symbology will be applied.
      in_symbology_layer (Layer):
          The layer containing the symbology that will be applied to the input
          layer. Both .lyrx and .lyr files are supported.
      symbology_fields {Value Table}:
          The fields from the input layer that match the symbology
          fields used in the symbology layer. Symbology fields contain three
          properties:        Field type-The field type: symbology value,
          normalization, or other
          type.Source field-The symbology field used by the symbology layer. Use
          a
          blank value or "#" if you do not know the source field and want to use
          the default.Target field-The field from the input layer to use when
          applying the
          symbology. Supported field types are as follows:
          VALUE_FIELD-Primary field used to symbolize
          valuesNORMALIZATION_FIELD-Field used to normalize quantitative
          valuesEXCLUSION_CLAUSE_FIELD-Field used for the symbology exclusion
          clauseCHART_RENDERER_PIE_SIZE_FIELD-Field used to set the size of pie
          chart
          symbolsROTATION_XEXPRESSION_FIELD-Field used to set the rotation of
          symbols
          on the x-axisROTATION_YEXPRESSION_FIELD-Field used to set the rotation
          of symbols
          on the y-axisROTATION_ZEXPRESSION_FIELD-Field used to set the rotation
          of symbols
          on the z-axisTRANSPARENCY_EXPRESSION_FIELD-Field used to set the
          transparency of
          symbolsTRANSPARENCY_NORMALIZATION_FIELD-Field used to normalize
          transparency
          valuesSIZE_EXPRESSION_FIELD-Field used to set the size or width of
          symbolsCOLOR_EXPRESSION_FIELD-Field used to set the color of
          symbolsPRIMITIVE_OVERRIDE_EXPRESSION_FIELD-Field used to set various
          properties on individual symbol layers
      update_symbology {String}:
          Specifies whether symbology ranges will be updated. DEFAULT-
          Symbology ranges will be updated,
          except in the following
          situations:          When the input layer is emptyWhen the symbology
          layer uses class
          breaks (for example, graduated
          colors or graduated symbols) and the classification method is manual
          or defined interval            When the symbology layer uses unique
          values and theoption
          is checked            Show all other valuesUPDATE-Symbology ranges
          will be updated.MAINTAIN-Symbology ranges will not be updated; they
          will be
          maintained.

        """