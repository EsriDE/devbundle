# Generated documentation for module arcpy.geoanalytics


class DissolveBoundaries(object):
    """
    Finds polygons that intersect or have the same field values and merges them to form a single polygon.
    """

    @property
    def description(self) -> str:
        return """

        DissolveBoundaries_geoanalytics(input_layer, output_name, {multipart}, {dissolve_fields}, {fields;fields...}, {summary_fields;summary_fields...}, {data_store})

        Finds polygons that intersect or have the same field values and merges
        them to form a single polygon.

     INPUTS:
      input_layer (Feature Set):
          The layer containing the polygon features that will be dissolved.
      output_name (String):
          The name of the output feature service.
      multipart {Boolean}:
          Specifies whether multipart features will be created in the output
          feature class.MULTI_PART-Multipart features will be
          created.SINGLE_PART-Multipart
          features will not be created. Individual
          features will be created for each part instead. This is the default.
      dissolve_fields {Boolean}:
          Specifies whether features with the same field values will be
          dissolved.NO_DISSOLVE_FIELDS-Polygons that share a common border (that
          is, they
          are adjacent) or polygons that overlap will be dissolved into one
          polygon. This is the default.DISSOLVE_FIELDS-Polygons that have the
          same field value or values will
          be dissolved.
      fields {Field}:
          The field or fields that will be used to dissolve like features.
          Features with the same value for each field will be dissolved.
      summary_fields {Value Table}:
          The statistics that will be calculated on specified fields.Count-The
          number of nonnull values. It can be used on numeric fields
          or strings. The count of [null, 0, 2] is 2.Sum-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.Mean-The mean of numeric values. The mean of [0, 2, null] is
          1.Min-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.Max-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.Standard Deviation-The standard deviation of a numeric
          field. The
          standard deviation of [1] is null. The standard deviation of [null,
          1,1,1] is null.Variance-The variance of a numeric field in a track.
          The variance of
          [1] is null. The variance of [null, 1, 1, 1] is null.Range-The range
          of a numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.Any-A sample string from a field of
          type string.The statistics that will be calculated on specified
          fields.COUNT-The number of nonnull values. It can be used on numeric
          fields
          or strings. The count of [null, 0, 2] is 2.SUM-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.MEAN-The mean of numeric values. The mean of [0,2, null] is
          1.MIN-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.MAX-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.STDDEV-The standard deviation of a numeric field. The
          standard
          deviation of [1] is null. The standard deviation of [null, 1,1,1] is
          null.VAR-The variance of a numeric field in a track. The variance of
          [1] is
          null. The variance of [null, 1,1,1] is null.RANGE-The range of a
          numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.ANY-A sample string from a field of
          type string.
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.

        """