# Generated documentation for module arcpy.cartography


class TiledLabelsToAnnotation(object):
    """
    Converts labels to annotation for layers in a map based on a polygon index layer.
    """

    @property
    def description(self) -> str:
        return """

        TiledLabelsToAnnotation_cartography(input_map, polygon_index_layer, out_geodatabase, out_layer, anno_suffix, {reference_scale_value}, {reference_scale_field}, {tile_id_field}, {coordinate_sys_field}, {map_rotation_field}, {feature_linked}, {generate_unplaced_annotation}, {which_layers}, {single_layer}, {require_symbol_id}, {auto_create}, {update_on_shape_change}, {multiple_feature_classes}, {merge_label_classes})

        Converts labels to annotation for layers in a map based on a polygon
        index layer.

     INPUTS:
      input_map (Map):
          The map that contains the labels to convert to annotation.
      polygon_index_layer (Table View):
          The polygon layer that contains tile features.
      out_geodatabase (Workspace / Feature Dataset):
          The workspace where the output feature classes will be saved. The
          workspace can be an existing geodatabase or an existing feature
          dataset.
      anno_suffix (String):
          The suffix that will be added to each new annotation feature class.
          This suffix will be appended to the name of the source feature class
          for each new annotation feature class. The reference scale for the
          annotation will follow this suffix.
      reference_scale_value {Double}:
          The scale value that will be used as a reference for the annotation.
          This is the scale on which all symbol and text sizes in the annotation
          will be based.
      reference_scale_field {Field}:
          The field in the polygon index layer that will determine the reference
          scale of the annotation. This is the scale on which all symbol and
          text sizes in the annotation will be based.
      tile_id_field {Field}:
          A field in the polygon index layer that uniquely identifies
          the tiled area. These values will populate thefield in the annotation
          feature class attribute table. TileID
      coordinate_sys_field {Field}:
          A field in the polygon index layer that contains the coordinate system
          information for each tile. Due to the length required for a field to
          store coordinate system information, a polygon index layer that
          contains a coordinate system field must be a geodatabase feature
          class.
      map_rotation_field {Field}:
          A field in the polygon index layer that contains the angle by which
          the map will be rotated.
      feature_linked {Boolean}:
          Specifies whether the output annotation feature class will be linked
          to the features in another feature class.STANDARD-The output
          annotation feature class will not be linked to
          the features in another feature class. This is the
          default.FEATURE_LINKED-The output annotation feature class will be
          linked to
          the features in another feature class.
      generate_unplaced_annotation {Boolean}:
          Specifies whether unplaced annotation will be created from unplaced
          labels.NOT_GENERATE_UNPLACED_ANNOTATION-Annotation will only be
          created for
          features that are currently labeled. This is the
          default.GENERATE_UNPLACED_ANNOTATION-Unplaced annotation will be
          stored in the
          annotation feature class. The status field for this annotation is set
          to Unplaced.
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
      require_symbol_id {Boolean}:
          Specifies whether all text symbol properties can be
          edited.NO_REQUIRE_ID-All text symbol properties can be edited. This is
          the
          default.REQUIRE_ID-Only symbol properties that enable annotation
          features can
          be edited to maintain reference to their associated text symbol in the
          collection.
      auto_create {Boolean}:
          Specifies whether annotation will be created when new features are
          added to the linked feature class if the feature_linked parameter is
          set to FEATURE_LINKED.AUTO_CREATE-Feature-linked annotation will be
          created when new
          features are added to the linked feature class. This is the
          default.NO_AUTO_CREATE-Feature-linked annotation will not be created
          when new
          features are added to the linked feature class.
      update_on_shape_change {Boolean}:
          Specifies whether the position of annotation will be updated when the
          shape of the linked feature is modified if the feature_linked
          parameter is set to FEATURE_LINKED.SHAPE_UPDATE-The position of the
          annotation will be updated when the
          shape of the linked feature is modified. This is the
          default.NO_SHAPE_UPDATE-The position of the annotation will not be
          updated
          when the shape of the linked feature is modified.
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
          Specifies whether similar label classes will be merged if the
          multiple_feature_classes parameter is set to
          SINGLE_FEATURE_CLASS.MERGE_LABEL_CLASS-Label classes with similar
          properties will be merged
          when converting to a single feature class.NO_MERGE_LABEL_CLASS-Label
          classes with similar properties will not be
          merged. This is the default.

     OUTPUTS:
      out_layer (Group Layer):
          The group layer that will contain the generated annotation. You can
          use the Save To Layer File tool to write the output group layer to a
          layer file.

        """