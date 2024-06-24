# Generated documentation for module arcpy.sfa


class CreateBuffers(object):
    """
    Creates polygons that cover a given distance from a point, line, or polygon feature.
    """

    @property
    def description(self) -> str:
        return """

        CreateBuffers_sfa(inputLayer, outputName, {distances;distances...}, {field}, {units}, {dissolveType}, {ringType}, {sideType}, {endType})

        Creates polygons that cover a given distance from a point, line, or
        polygon feature.

     INPUTS:
      inputLayer (Feature Set):
          The point, line, or polygon features to be buffered.
      outputName (String):
          The name of the output layer to create on your portal.
      distances {Double}:
          A list of distance values to buffer the input features. You must
          supply values for either the distances or a distance field. You can
          enter a single distance value or multiple values. The units of the
          distance values is supplied by the distance units.
      field {Field}:
          A field from the input layer containing one buffer distance per
          feature.
      units {String}:
          The units of the buffer distance. You must provide a value if cell
          size has been set.MILES-MilesFEET-FeetKILOMETERS-KilometersMETERS-Mete
          rsNAUTICALMILES-Na
          utical milesYARDS-Yards
      dissolveType {String}:
          Determines how overlapping buffers are processed.NONE-Overlapping
          areas are kept. This is the default.DISSOLVE-
          Overlapping areas are combined.
      ringType {String}:
          Determines how multiple-distance buffers are processed.DISKS-Buffers
          are concentric and will overlap. For example, if your
          distances are 10 and 14, the result will be two buffers, one from 0 to
          10 and one from 0 to 14. This is the default.RINGS-Buffers will not
          overlap. For example, if your distances are 10
          and 14, the result will be two buffers, one from 0 to 10 and one from
          10 to 14.
      sideType {String}:
          When buffering line features, you can choose which side of the
          line to buffer. Typically, you choose both sides (, which is the
          default). Left and right are determined as if you were walking from
          the first x, y coordinate of the line (the start coordinate) to the
          last x,y coordinate of the line (the end coordinate). Choosing left or
          right usually means you know that your line features were created and
          stored in a particular direction (for example, upstream or downstream
          in a river network). FullWhen buffering polygon features, you
          can choose whether the buffer
          includes or excludes the polygon being buffered.If a side type is not
          supplied, the polygon being buffered is included
          in the result buffer. This is the default for polygon features.FULL-
          Both sides of the line will be buffered. This is the default for
          line features.RIGHT-Only the right side of the line will be
          buffered.LEFT-Only the left side of the line will be
          buffered.OUTSIDE-When buffering a polygon, the polygon being buffered
          is
          excluded in the result buffer.
      endType {String}:
          The shape of the buffer at the end-of-line input features. This
          parameter is not valid for polygon input features. At the ends of
          lines, the buffer can be rounded (round) or be straight across
          (flat).ROUND-Buffers will be rounded at the ends of lines. This is
          the
          default.FLAT-Buffers will be flat or straight across at the ends of
          lines.

        """