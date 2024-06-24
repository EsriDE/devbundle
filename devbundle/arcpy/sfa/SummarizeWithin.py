# Generated documentation for module arcpy.sfa


class SummarizeWithin(object):
    """
    Finds the point, line, or polygon features (or portions of these features) that are within the boundaries of polygons in another layer.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeWithin_sfa(sumWithinLayer, summaryLayer, outputName, {sumShape}, {shapeUnits}, {summaryFields;summaryFields...}, {groupByField}, {minorityMajority}, {percentShape})

        Finds the point, line, or polygon features (or portions of these
        features) that are within the boundaries of polygons in another layer.

     INPUTS:
      sumWithinLayer (Feature Set):
          Features, or portions of features, in the input summary features that
          fall within the boundaries of these polygons will be summarized.
      summaryLayer (Feature Set):
          The point, line, or polygon features that will be summarized for each
          input polygon.
      outputName (String):
          The name of the output layer to create on your portal.
      sumShape {Boolean}:
          Calculate statistics based on the shape of the input summary features,
          such as the length of lines or areas of polygons of the input summary
          features within each input polygon.ADD_SHAPE_SUM-Calculate the shape
          summary attributes. This is the
          default.NO_SHAPE_SUM-Do not calculate the shape summary attributes.
      shapeUnits {String}:
          If summarizing the shape of the input summary features, specify the
          units of the shape summary.When the input summary features are
          polygons, the valid options are
          acres, hectares, square meters, square kilometers, square feet, square
          yards, and square miles.When the input summary features are lines, the
          valid options are
          meters, kilometers, feet, yards, and miles.MILES-MilesFEET-FeetKILOMET
          ERS-KilometersMETERS-MetersYARDS-YardsACRES
          -AcresHECTARES-HectaresSQUAREMETERS-Square
          metersSQUAREKILOMETERS-Square kilometersSQUAREFEET-Square
          feetSQUAREYARDS-Square yardsSQUAREMILES-Square miles
      summaryFields {Value Table}:
          A list of field names and statistical summary type that you
          wish to calculate for all points within each polygon. The count of
          points within each polygon is always returned. The following statistic
          types are supported:        SUM-The total value.MIN-The smallest
          value.MAX-The largest
          value.MEAN-The average or mean value.STD-The standard deviation.
      groupByField {Field}:
          This is a field from the input summary features that you can
          use to calculate statistics separately for each unique attribute
          value. For example, suppose the input summary features contain point
          locations of businesses that store hazardous materials, and one of the
          fields iscontaining codes that describe the type of hazardous material
          stored. To calculate summaries by each unique value of, use it as the
          group by field. HazardClassHazardClass
      minorityMajority {Boolean}:
          This only applies when using a group by field. If you specify
          ADD_MIN_MAJ, the minority (least dominant) or the majority (most
          dominant) attribute values for each group field within each boundary
          are calculated. Two new fields are added to the output layer prefixed
          with Majority_ and Minority_.NO_MIN_MAJ-Do not add minority and
          majority fields. This is the
          default.ADD_MIN_MAJ-Add minority and majority fields.
      percentShape {Boolean}:
          This only applies when using a group by field. If checked, the
          percentage of each unique group value is calculated for each input
          polygon.NO_PERCENT-Do not add percentage fields. This is the
          default.ADD_PERCENT-Add percentage fields.

        """