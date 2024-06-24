# Generated documentation for module arcpy.cartography


class DetectGraphicConflict(object):
    """
    Creates polygons where two or more symbolized features graphically conflict.
    """

    @property
    def description(self) -> str:
        return """

        DetectGraphicConflict_cartography(in_features, conflict_features, out_feature_class, {conflict_distance}, {line_connection_allowance})

        Creates polygons where two or more symbolized features graphically
        conflict.

     INPUTS:
      in_features (Layer):
          The input feature layer containing symbolized features. CAD, coverage,
          or VPF annotation, and dimensions, charts, dot-density or proportional
          symbols, raster layers, network datasets, and 3D symbols are not
          acceptable inputs.
      conflict_features (Layer):
          The feature layer containing symbolized features potentially in
          conflict with symbolized features in the input layer.
      conflict_distance {Linear Unit}:
          The area where input and conflict symbology is closer than a certain
          distance. Temporary buffers one-half the size of the conflict distance
          value are created around symbols in both the input and conflict
          layers. Conflict polygons will be generated where these buffers
          overlap. Conflict distance is measured in page units (points, inches,
          millimeters, or centimeters). If you enter a conflict distance in map
          units, it will be converted to page units using the reference scale.
          The default conflict distance is 0, where no buffers are created and
          only symbols that physically overlap one another are detected as
          conflicts.
      line_connection_allowance {Linear Unit}:
          The radius of a circle, centered where lines join, within which
          graphic overlaps won't be detected. This parameter is only considered
          when the input layer and the conflict layer are identical. Zero
          allowance will detect a conflict at each line join (if end caps are
          overlapping). Line connection allowance is calculated in page units
          (points, inches, millimeters, or centimeters). If you enter an
          allowance in map units, it will be converted to page units using the
          reference scale. The value cannot be negative; the default value is 1
          point.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created to store conflict polygons. It
          cannot be one of the feature classes associated with the input layers.

        """