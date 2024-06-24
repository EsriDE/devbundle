# Generated documentation for module arcpy.sfa


class OverlayLayers(object):
    """
    Overlays the geometries from multiple layers into one single layer. Overlay can be used to combine, erase, modify, or update spatial features. Overlay is much more than a merging of geometries; all the attributes of the features taking part in the overlay are carried through to the result.
    """

    @property
    def description(self) -> str:
        return """

        OverlayLayers_sfa(inputLayer, overlayLayer, outputName, {overlayType}, {outputType}, {snapToInput}, {tolerance})

        Overlays the geometries from multiple layers into one single layer.
        Overlay can be used to combine, erase, modify, or update spatial
        features. Overlay is much more than a merging of geometries; all the
        attributes of the features taking part in the overlay are carried
        through to the result.

     INPUTS:
      inputLayer (Feature Set):
          The point, line, or polygon features that will be overlaid with the
          overlay layer.
      overlayLayer (Feature Set):
          The features that will be overlaid with the input layer features.
      outputName (String):
          The name of the output layer to create on your portal.
      overlayType {String}:
          The type of overlay to be performed.INTERSECT-Computes a geometric
          intersection of the input layers.
          Features or portions of features that overlap in both the input layer
          and overlay layer will be written to the output layer. This is the
          default.UNION-Computes a geometric union of the input layers. All
          features and
          their attributes will be written to the output layer. This option is
          only valid if both the input layer and the overlay layer contain
          polygon features.ERASE-Only those features or portions of features in
          the overlay layer
          that are not within the features in the input layer are written to the
          output.
      outputType {String}:
          The type of intersection you want to find. This parameter is only
          valid when the overlay type is Intersect.INPUT-The features returned
          will be the same geometry type as the
          input layer or overlay layer with the lowest dimension geometry. If
          all inputs are polygons, the output will contain polygons. If one or
          more of the inputs are lines and none of the inputs are points, the
          output will be line. If one or more of the inputs are points, the
          output will contain points. This is the default.LINE-Line
          intersections will be returned. This is only valid if none
          of the inputs are points.POINT-Point intersections will be returned.
          If the inputs are line or
          polygon, the output will be a multipoint layer.
      snapToInput {Boolean}:
          Specifies if feature vertices in the input layer are allowed to move.
          The default is NO_SNAP and means if the distance between features is
          less than the tolerance value, all features from both layers can move
          to allow snapping to each other. When the value is SNAP, only features
          in the overlay layer can move to snap to the input layer
          features.NO_SNAP-Allow features from both layers to snap their
          vertices to each
          other. This is the default.SNAP-Only allow features in the overlay
          layer to move vertices to snap
          to the input layer.
      tolerance {Double}:
          A double value of the minimum distance separating all feature
          coordinates as well as the distance a coordinate can move in X or Y
          (or both). The units of tolerance are the same as the units of the
          input layer's coordinate system.

        """