# Generated documentation for module arcpy.conversion


class GraphicsToFeatures(object):
    """
    Converts a graphics layer into a feature layer with geometries based on the input graphics layer's elements.
    """

    @property
    def description(self) -> str:
        return """

        GraphicsToFeatures_conversion(in_layer, graphics_type, out_feature_class, {delete_graphics}, {reference_scale})

        Converts a graphics layer into a feature layer with geometries based
        on the input graphics layer's elements.

     INPUTS:
      in_layer (Graphics Layer):
          The graphics layer containing the source graphic elements that will be
          converted to features.
      graphics_type (String):
          Specifies the type of graphic element that will be
          converted.POINT-Point graphic elements will be
          converted.POLYLINE-Polyline
          graphic elements will be converted.POLYGON-Polygon graphic elements
          will be converted.MULTIPOINT-Multipoint graphic elements will be
          converted.ANNOTATION-Annotation and text graphic elements will be
          converted.
      delete_graphics {Boolean}:
          Specifies whether the converted graphic elements from the in_layer
          parameter will be deleted after conversion.DELETE_GRAPHICS-The
          converted graphic elements will be deleted. This
          is the default.KEEP_GRAPHICS-The converted graphic elements will not
          be deleted; they
          will be preserved.
      reference_scale {Double}:
          The reference scale that will be used to convert text elements to
          annotation features. This parameter is required when the graphics_type
          parameter is set to ANNOTATION.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature layer that will contain the converted graphic
          elements.

        """