# Generated documentation for module arcpy.ra


class CreateViewshed(object):
    """
    Creates areas where an observer can see objects on the ground. The input observer points can represent either observers (such as people on the ground or lookouts in a fire tower) or observed objects (such as wind turbines, water towers, vehicles, or other people).
    """

    @property
    def description(self) -> str:
        return """

        CreateViewshed_ra(inputElevationSurface, inputObserverFeatures, outputName, {optimizeFor}, {maximumViewingDistanceType}, {maximumViewingDistance}, {maximumViewingDistanceField}, {minimumViewingDistanceType}, {minimumViewingDistance}, {minimumViewingDistanceField}, {viewingDistanceIs3D}, {observersElevationType}, {observersElevation}, {observersElevationField}, {observersHeightType}, {observersHeight}, {observersHeightField}, {targetHeightType}, {targetHeight}, {targetHeightField}, {aboveGroundLevelOutputName}, {verticalError}, {refractivityCoefficient}, {horizontalStartAngle}, {horizontalEndAngle}, {verticalUpperAngle}, {verticalLowerAngle})

        Creates areas where an observer can see objects on the ground. The
        input observer points can represent either observers (such as people
        on the ground or lookouts in a fire tower) or observed objects (such
        as wind turbines, water towers, vehicles, or other people).

     INPUTS:
      inputElevationSurface (Image Service / Raster Layer / String):
          The elevation surface that will be used for calculating the
          viewshed.If the vertical unit of the input surface is different from
          the
          horizontal unit, such as when the elevation values are represented in
          feet but the coordinate system is in meters, the surface must have a
          defined vertical coordinate system. This is because the tool uses the
          vertical (z) and horizontal (x,y) units to compute a z-factor for the
          viewshed analysis. Without a vertical coordinate system, and having no
          z-unit information available, it is assumed that the z-unit is the
          same as the x,y unit. The result is an internal z-factor of 1.0 will
          be used for the analysis, which may give unexpected results.The
          elevation surface can be integer or floating point.
      inputObserverFeatures (Feature Set):
          The point features that represent the observer locations when
          calculating the viewsheds.
      outputName (String):
          The name of the output raster service.The default name is based on the
          tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      optimizeFor {String}:
          Specifies the optimization method that will be used to calculate the
          viewshed.SPEED-Processing speed will be optimized, trading some
          accuracy in the
          result for better performance. This is the default.ACCURACY-Accuracy
          in the results will be optimized, at the expense of
          a longer processing time.
      maximumViewingDistanceType {String}:
          Specifies how the maximum viewing distance will be
          determined.DISTANCE-The maximum distance will be determined by the
          value you
          specify. This is the default method.FIELD-The maximum distance for
          each observer location will be
          determined by the values in a field you specify.
      maximumViewingDistance {Linear Unit}:
          The cutoff distance that will be used where the computation of visible
          areas stops. Beyond this distance, it is unknown whether the observer
          points and the other objects can see each other.The unit values are
          Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.The default value is 9 statute miles.
      maximumViewingDistanceField {Field}:
          The field containing the maximum viewing distance for each observer.
          The values contained in the field must be in the same unit as the x,y
          unit of the input elevation surface.The maximum viewing distance is a
          cutoff distance where the
          computation of visible areas stops. Beyond this distance, it is
          unknown whether the observer points and the other objects can see each
          other.
      minimumViewingDistanceType {String}:
          Specifies how the minimum visible distance will be
          determined.DISTANCE-The minimum distance will be determined by the
          value you
          specify. This is the default method.FIELD-The minimum distance for
          each observer location will be
          determined by the values in a field you specify.
      minimumViewingDistance {Linear Unit}:
          The distance that will be used where the computation of visible areas
          begins. Cells on the surface closer than this distance are not visible
          in the output but can still block visibility of the cells between the
          minimum and maximum viewing distance.The unit values are Kilometers,
          Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.
      minimumViewingDistanceField {Field}:
          The field containing the minimum viewing distance for each observer.
          The values contained in the field must be in the same unit as the
          x,y-unit of the input elevation surface.The minimum viewing distance
          defines where the computation of visible
          areas begins. Cells on the surface closer than this distance are not
          visible in the output but can still block visibility of the cells
          between the minimum and maximum viewing distance.
      viewingDistanceIs3D {Boolean}:
          Specifies whether the minimum and maximum viewing distance parameter
          values will be measured in 3D or 2D. A 2D distance is the simple
          linear distance measured between an observer and the target using
          their projected locations at sea level. A 3D distance provides a more
          realistic value by taking their relative heights into
          consideration.2D-The viewing distance will be measured in 2D distance.
          This is the
          default.3D-The viewing distance will be measured in 3D distance.
      observersElevationType {String}:
          Specifies how the elevation of the observers will be
          determined.ELEVATION-The observer elevation will be determined by the
          value you
          specify. This is the default method.FIELD-The elevation for each
          observer location will be determined by
          the values in a field you specify.
      observersElevation {Linear Unit}:
          The elevation that will be used for the observer locations.If this
          parameter is not specified, the observer elevation will be
          obtained from the surface raster using bilinear interpolation. If this
          parameter is set to a value, that value will be applied to all the
          observers. To specify different values for each observer, set this
          parameter to a field in the input observer features.The unit values
          are Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.
      observersElevationField {Field}:
          The field containing the elevation for the observers. The value
          contained in the field must be in the same unit as the z-unit of the
          input elevation surface.If this parameter is not specified, the
          observer elevation will be
          obtained from the surface raster using bilinear interpolation.
      observersHeightType {String}:
          Specifies how the height of the observers will be
          determined.HEIGHT-The observer height will be determined by the value
          you
          specify. This is the default method.FIELD-The height for each observer
          location will be determined by the
          values in a field you specify.
      observersHeight {Linear Unit}:
          The height that will be used for the observer locations.The unit
          values are Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.The default value is 6 international feet.
      observersHeightField {Field}:
          The field containing the height for the observers. The value contained
          in the field must be in the same unit as the z-unit of the input
          elevation surface.
      targetHeightType {String}:
          Specifies how the target height will be determined.HEIGHT-The target
          height will be determined by the value you specify.
          This is the default method.FIELD-The height for each target will be
          determined by the values in a
          field you specify.
      targetHeight {Linear Unit}:
          The height of structures or people on the ground that will be used to
          establish visibility. The result viewshed are those areas where an
          observer point can see these other objects. The converse is also true;
          the other objects can see an observer point.The unit values are
          Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.
      targetHeightField {Field}:
          The field containing the height for the targets. The value contained
          in the field must be in the same unit as the z-unit of the input
          elevation surface.
      aboveGroundLevelOutputName {String}:
          The name of the output above-ground-level (AGL) raster. The AGL result
          is a raster in which each cell value is the minimum height that must
          be added to an otherwise nonvisible cell to make it visible by at
          least one observer. Cells that were already visible will be assigned 0
          in this output raster.
      verticalError {Linear Unit}:
          The amount of uncertainty (the root mean square (RMS) error) in the
          surface elevation values. It is a floating-point value representing
          the expected error of the input elevation values.When this parameter
          is assigned a value greater than 0, the output
          visibility raster will be floating point.
      refractivityCoefficient {Double}:
          The coefficient of the refraction of visible light in air.The default
          value is 0.13.
      horizontalStartAngle {String}:
          The start angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 0.You can select a
          field in the input observer features, or you can
          provide a numerical value.
      horizontalEndAngle {String}:
          The end angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 360.You can select a
          field in the input observer features, or you can
          provide a numerical value.
      verticalUpperAngle {String}:
          The upper vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from above -90 up to and including
          90. The value can be integer or floating point. The default value is
          90 (straight up).You can select a field in the input observer
          features, or you can
          provide a numerical value.
      verticalLowerAngle {String}:
          The lower vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from -90 up to but not including
          90. The value can be integer or floating point. The default value is
          -90 (straight down).You can select a field in the input observer
          features, or you can
          provide a numerical value.

        """