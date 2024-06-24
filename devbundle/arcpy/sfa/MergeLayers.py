# Generated documentation for module arcpy.sfa


class MergeLayers(object):
    """
    Copies all features from two layers into a new layer. The layers to be combined must contain the same feature types (points, lines, or polygons). You can control how the fields from the input layers are joined and copied.
    """

    @property
    def description(self) -> str:
        return """

        MergeLayers_sfa(inputLayer, mergeLayer, outputName, {mergingAttributes;mergingAttributes...})

        Copies all features from two layers into a new layer. The layers to be
        combined must contain the same feature types (points, lines, or
        polygons). You can control how the fields from the input layers are
        joined and copied.

     INPUTS:
      inputLayer (Feature Set):
          The point, line, or polygon features to merge with the merge layer.
      mergeLayer (Feature Set):
          The point, line, or polygon features to merge with the input layer.
          The merge layer must contain the same feature type (point, line, or
          polygon) as the input layer.
      outputName (String):
          The name of the output layer to create on your portal.
      mergingAttributes {Value Table}:
          A list of values that describe how fields from the merge layer are to
          be modified and matched with fields in the input layer. By default,
          all fields from both inputs will be carried across to the output
          layer. If a field exists in one layer but not the other, the
          output
          layer will contain both fields. The output field will contain null
          values for the input features that did not have the field. For
          example, if the input layer contains a field namedbut the merge layer
          does not contain, the output will contain, but its values will be null
          for all the features copied from the merge layer. TYPETYPETYPE
          You can control the following merge actions (how fields on the
          merge layer are written to the output). REMOVE-The merge layer
          field will be removed from the output
          layer.RENAME-The merge layer field will be renamed in the output. You
          cannot
          rename a field from the merge layer to a field from the input layer.
          If you want to make field names equivalent, use the match option.
          MATCH-The merge layer field is renamed and matched to a
          field from the input layer. For example, the input layer has a field
          namedand the merge layer has a field named. You can matchto, and the
          output will contain thefield with values of thefield used for features
          copied from the merge layer. Type casting is supported (for example,
          double to integer, integer to string), except for string to numeric.
          CODESTATUSSTATUSCODECODESTATUS

        """