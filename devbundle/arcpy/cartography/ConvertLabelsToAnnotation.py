# Generated documentation for module arcpy.cartography


class ConvertLabelsToAnnotation(object):
    """
    Converts labels to annotation for a single layer or the entire map. Both standard annotation and feature-linked annotation can be created.
    """

    @property
    def description(self) -> str:
        return """

        ConvertLabelsToAnnotation_cartography(input_map, conversion_scale, output_geodatabase, {anno_suffix}, {extent}, {generate_unplaced}, {require_symbol_id}, {feature_linked}, {auto_create}, {update_on_shape_change}, {output_group_layer}, {which_layers}, {single_layer}, {multiple_feature_classes}, {merge_label_classes})

        Converts labels to annotation for a single layer or the entire map.
        Both standard annotation and feature-linked annotation can be created.

     INPUTS:
      input_map (Map):
          The input map.
      conversion_scale (Double):
          The scale at which labels will be converted. If a reference scale is
          set on the map, the reference scale will be used for symbol sizing and
          annotation feature class creation, but conversion will occur at this
          scale.
      output_geodatabase (LocalDatabase|RemoteDatabase):
          The workspace where the output feature classes will be saved. The
          workspace can be an existing geodatabase or an existing feature
          dataset. If this is not the same database used by all the layers in
          the map, the feature-linked option will be disabled.
      anno_suffix {String}:
          The suffix that will be added to each new annotation feature class.
          This suffix will be appended to the name of the source feature class
          for each new annotation feature class.
      extent {Extent}:
          Specifies the extent that contains the labels to convert to
          annotation.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.If no extent value is set, the extent will be
          based on the maximum
          extent of all participating inputs. This is the default.
      generate_unplaced {Boolean}:
          Specifies whether unplaced annotation will be created from unplaced
          labels.ONLY_PLACED-Annotation will only be created for features that
          are
          currently labeled. This is the default.GENERATE_UNPLACED-Unplaced
          annotation will be stored in the annotation
          feature class. The status field for this annotation is set to
          Unplaced.
      require_symbol_id {Boolean}:
          Specifies whether all text symbol properties can be
          edited.NO_REQUIRE_ID-All text symbol properties can be edited. This is
          the
          default.REQUIRE_ID-Only symbol properties that enable annotation
          features can
          be edited to maintain reference to their associated text symbol in the
          collection.
      feature_linked {Boolean}:
          Specifies whether the output annotation feature class will be linked
          to the features in another feature class.STANDARD-The output
          annotation feature class will not be linked to the
          features in another feature class. This is the
          default.FEATURE_LINKED-The output annotation feature class will be
          linked to
          the features in another feature class.
      auto_create {Boolean}:
          Specifies whether annotation will be created when new features are
          added to the linked feature class and the feature_linked parameter is
          set to FEATURE_LINKED.AUTO_CREATE-Feature-linked annotation will be
          created when new
          features are added to the linked feature class. This is the
          default.NO_AUTO_CREATE-Feature-linked annotation will not be created
          when new
          features are added to the linked feature class.
      update_on_shape_change {Boolean}:
          Specifies whether the position of annotation will be updated when the
          shape of the linked feature is modified and the feature_linked
          parameter is set to FEATURE_LINKED.SHAPE_UPDATE-The position of the
          annotation will be updated when the
          shape of the linked feature is modified. This is the
          default.NO_SHAPE_UPDATE-The position of the annotation will not be
          updated
          when the shape of the linked feature is modified.
      which_layers {String}:
          Specifies whether annotation will be converted for all layers in the
          map or for a single layer. The single layer must be
          specified.ALL_LAYERS-Labels will be converted to annotation for all
          layers in
          the map. This is the default.SINGLE_LAYER-Labels will be converted to
          annotation for a single
          layer. The layer must be specified.
      single_layer {Feature Layer}:
          The layer with the annotation that will be converted when the
          which_layers parameter is set to SINGLE_LAYER. This layer must be in
          the map.
      multiple_feature_classes {Boolean}:
          Specifies whether labels will be converted to individual annotation
          feature classes or to a single annotation feature class. If converting
          to a single annotation feature class, the annotation cannot be
          feature-linked.SINGLE_FEATURE_CLASS-Labels from all layers will be
          converted to a
          single annotation feature class.FEATURE_CLASS_PER_FEATURE_LAYER-Labels
          will be converted to individual
          annotation feature classes that correspond to their layers. This is
          the default.
      merge_label_classes {Boolean}:
          Specifies whether similar label classes will be merged when the
          multiple_feature_classes parameter is set to
          SINGLE_FEATURE_CLASS.MERGE_LABEL_CLASS-Label classes with similar
          properties will be merged
          when converting to a single feature class.NO_MERGE_LABEL_CLASS-Label
          classes with similar properties will not be
          merged. This is the default.

     OUTPUTS:
      output_group_layer {Group Layer}:
          The group layer that will contain the generated annotation. You can
          use the Save To Layer File tool to write the output group layer to a
          layer file.

        """