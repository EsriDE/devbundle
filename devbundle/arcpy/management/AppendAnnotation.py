# Generated documentation for module arcpy.management


class AppendAnnotation(object):
    """
    Creates a geodatabase annotation feature class or appends to an existing annotation feature class by combining annotation from multiple input geodatabase annotation feature classes into a single feature class with annotation classes.
    """

    @property
    def description(self) -> str:
        return """

        AppendAnnotation_management(input_features;input_features..., output_featureclass, reference_scale, {create_single_class}, {require_symbol_from_table}, {create_annotation_when_feature_added}, {update_annotation_when_feature_modified})

        Creates a geodatabase annotation feature class or appends to an
        existing annotation feature class by combining annotation from
        multiple input geodatabase annotation feature classes into a single
        feature class with annotation classes.

     INPUTS:
      input_features (Feature Layer):
          The input annotation features that will form an annotation class in
          the output feature class.
      reference_scale (Double):
          The reference scale set in the output feature class. Input features
          created at a different reference scale will be transformed to match
          this output reference scale.
      create_single_class {Boolean}:
          Specifies how annotation features will be added to the output feature
          class.ONE_CLASS_ONLY-All annotation features will be aggregated into
          one
          annotation class in the output feature class.CREATE_CLASSES-Separate
          annotation classes will be created for each
          input annotation class in the output feature class unless the classes
          are named the same and have the same properties. In this case, they
          will be merged. This is the default.
      require_symbol_from_table {Boolean}:
          Specifies how symbols can be selected for newly created annotation
          features.REQUIRE_SYMBOL-Only the list of symbols in the symbol
          collection of
          the output feature class can be used when creating annotation
          features.NO_SYMBOL_REQUIRED-Any symbology can be used when creating
          annotation
          features. This is the default.
      create_annotation_when_feature_added {Boolean}:
          Specifies whether feature-linked annotation will be created when a
          feature is added.AUTO_CREATE-Feature-linked annotation will be created
          using the label
          engine when a linked feature is added. The is the
          default.NO_AUTO_CREATE-Feature-linked annotation will not be created
          when a
          feature is added.
      update_annotation_when_feature_modified {Boolean}:
          Specifies whether feature-linked annotation will be updated when a
          linked feature changes.AUTO_UPDATE-Feature-linked annotation will be
          updated using the label
          engine when a linked feature changes. This is the
          default.NO_AUTO_UPDATE-Feature-linked annotation will not be updated
          when a
          linked feature changes.

     OUTPUTS:
      output_featureclass (Feature Class):
          A new or existing annotation feature class that will contain an
          annotation class for each input annotation feature class.

        """