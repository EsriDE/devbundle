# Generated documentation for module arcpy.analysis


class MultipleRingBuffer(object):
    """
    Creates multiple buffers at specified distances around the input features. These buffers can be merged and dissolved using the buffer distance values to create nonoverlapping buffers.
    """

    @property
    def description(self) -> str:
        return """

        MultipleRingBuffer_analysis(Input_Features, Output_Feature_class, Distances;Distances..., {Buffer_Unit}, {Field_Name}, {Dissolve_Option}, {Outside_Polygons_Only}, {Method})

        Creates multiple buffers at specified distances around the input
        features. These buffers can be merged and dissolved using the buffer
        distance values to create nonoverlapping buffers.

     INPUTS:
      Input_Features (Feature Layer):
          The input point, line, or polygon features to be buffered.
      Distances (Double):
          The list of buffer distances.
      Buffer_Unit {String}:
          Specifies the linear unit that will be used with the distance
          values.Default-The linear unit of the input features' spatial
          reference will
          be used. If the Output Coordinate System geoprocessing environment has
          been set, the linear unit of the environment will be used. The linear
          unit is ignored if the input features have an unknown or undefined
          spatial reference. This is the default.Inches-The unit will be
          inches.Feet-The unit will be feet.Yards-The unit will be
          yards.Miles-The unit will be miles.NauticalMiles-The unit will be
          nautical miles.Millimeters-The unit will be
          millimeters.Centimeters-The unit will be centimeters.Decimeters-The
          unit will be decimeters.Meters-The unit will be meters.Kilometers-The
          unit will be kilometers.DecimalDegrees-The unit will be decimal
          degrees.Points-The unit will be points.
      Field_Name {String}:
          The name of the field in the output feature class that will
          store the buffer distance used to create each buffer feature. The
          default is. The field will be of type Double. distance
      Dissolve_Option {String}:
          Specifies whether buffers will be dissolved to resemble rings around
          the input features.ALL-Buffers will be dissolved to resemble rings
          around the input
          features that do not overlap (think of these as rings or donuts around
          the input features). The smallest buffer will cover the area of its
          input feature plus the buffer distance, and subsequent buffers will be
          rings around the smallest buffer that do not cover the area of the
          input feature or smaller buffers. All buffers of the same distance
          will be dissolved into a single feature. This is the
          default.NONE-Buffers will not be dissolved. All buffer areas will be
          maintained regardless of overlap. Each buffer will cover its input
          feature plus the area of any smaller buffers.
      Outside_Polygons_Only {Boolean}:
          Specifies whether the buffers will cover the input features. This
          parameter is valid only for polygon input features.FULL-Buffers will
          overlap or cover the input features. This is the
          default.OUTSIDE_ONLY-Buffers will be rings around the input features,
          and will
          not overlap or cover the input features (the area inside the input
          polygon will be erased from the buffer).
      Method {String}:
          Specifies the method used to create the buffer.PLANAR-Buffers will be
          created using a Euclidean buffer method. This
          is the default when the input has a projected coordinate
          system.GEODESIC-Buffers will be created using a shape-preserving
          geodesic
          buffer method. This is the default when the input has a geographic
          coordinate system.

     OUTPUTS:
      Output_Feature_class (Feature Class):
          The output feature class that will contain multiple buffers.

        """