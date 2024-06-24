# Generated documentation for module arcpy.cartography


class ConvertLabelsToGraphics(object):
    """
    Converts labels to graphics for a single layer or an entire map.
    """

    @property
    def description(self) -> str:
        return """

        ConvertLabelsToGraphics_cartography(input_map, conversion_scale, {which_layers}, {single_layer}, {graphics_suffix}, {extent}, {multiple_graphics_layers}, {generate_unplaced}, {output_group_layer})

        Converts labels to graphics for a single layer or an entire map.

     INPUTS:
      input_map (Map):
          The input map object.
      conversion_scale (Double):
          The scale at which to convert labels. If a reference scale is set on
          the map, the reference scale will be used for symbol sizing and
          graphics layer creation, but conversion will happen at this scale.
      which_layers {String}:
          Specifies whether to convert graphics for all layers in the map or for
          a single layer.ALL_LAYERS-Labels will be converted to graphics for all
          layers in the
          map. This is the default. SINGLE_LAYER-Labels will be
          converted to graphics for a
          single layer. The layer must be specified in theparameter
          (single_layer in Python). Feature Layer
      single_layer {Feature Layer}:
          The layer with the labels to convert when the which_layers parameter
          is set to SINGLE_LAYER. This layer must be in the map.
      graphics_suffix {String}:
          The suffix that will be added to each new graphics layer. This suffix
          will be appended to the name of the source feature class for each new
          graphics layer.
      extent {Extent}:
          Specifies the extent that contains the labels to convert to
          graphics.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      multiple_graphics_layers {Boolean}:
          Specifies whether labels will be converted to individual graphics
          layers or to a single graphics layer.SINGLE_GRAPHICS_LAYER-Labels from
          all layers will be converted to a
          single graphics layer.GRAPHICS_LAYER_PER_FEATURE_LAYER-Labels will be
          converted to
          individual graphics layers that correspond to their layers. This is
          the default.
      generate_unplaced {Boolean}:
          Specifies whether graphics will be created from unplaced
          labels.ONLY_PLACED-Graphics will only be created for features that are
          currently labeled. This is the default.GENERATE_UNPLACED-Unplaced
          graphics are stored in the graphics layer
          with their visibility is turned off.

     OUTPUTS:
      output_group_layer {Group Layer}:
          The group layer that will contain the generated graphics. You can use
          the Save To Layer File tool to write the output group layer to a layer
          file.

        """