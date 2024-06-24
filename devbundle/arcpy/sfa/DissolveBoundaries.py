# Generated documentation for module arcpy.sfa


class DissolveBoundaries(object):
    """
    Finds polygons that overlap or share a common boundary and merges them together to form a single polygon.
    """

    @property
    def description(self) -> str:
        return """

        DissolveBoundaries_sfa(inputLayer, outputName, {dissolveFields;dissolveFields...}, {summaryFields;summaryFields...})

        Finds polygons that overlap or share a common boundary and merges them
        together to form a single polygon.

     INPUTS:
      inputLayer (Feature Set):
          The layer containing polygon features that will be dissolved or
          combined.
      outputName (String):
          The name of the output layer to create on your portal.
      dissolveFields {Field}:
          One or more fields from the input layer that control which polygons
          are merged. If you don't supply dissolve fields, polygons that share a
          common border (that is, they are adjacent) or polygon areas that
          overlap will be dissolved into one polygon. If you do supply
          fields, polygons that share a common border
          and contain the same value in one or more fields will be dissolved.
          For example, if you have a layer of counties and each county has
          aattribute, you can dissolve boundaries using theattribute. Adjacent
          counties will be merged together if they have the same value for. The
          end result is a layer of state boundaries. If two or more fields are
          specified, the values in these fields must be the same for the
          boundary to be dissolved. State_NameState_NameState_Name
      summaryFields {Value Table}:
          A list of field names and statistical summary type that you
          wish to calculate for all points within each polygon. The count of
          points within each polygon is always returned. The following statistic
          types are supported:        SUM-The total value.MIN-The smallest
          value.MAX-The largest
          value.MEAN-The average or mean value.STDDEV-The standard deviation.

        """