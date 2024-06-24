# Generated documentation for module arcpy.sfa


class SummarizeNearby(object):
    """
    Finds features that are within a specified distance of features in the input layer.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeNearby_sfa(sumNearbyLayer, summaryLayer, outputName, nearType, distances;distances..., units, {timeOfDay}, {timeZoneForTimeOfDay}, {returnBoundaries}, {sumShape}, {shapeUnits}, {summaryFields;summaryFields...}, {groupByField}, {minorityMajority}, {percentShape})

        Finds features that are within a specified distance of features in the
        input layer.

     INPUTS:
      sumNearbyLayer (Feature Set):
          Point, line, or polygon features from which distances will be measured
          to features in the input summary layer.
      summaryLayer (Feature Set):
          Point, line, or polygon features. Features in this layer that are
          within the specified distance to features in the input nearby layer
          will be summarized.
      outputName (String):
          The name of the output layer to create on your portal.
      nearType (String):
          Defines what kind of distance measurement you want to use: straight-
          line distance or by measuring travel time or travel distance along a
          street network using various modes of transportation known as travel
          modes.STRAIGHTLINE-Use straight-line Euclidean measurement of
          distance. This
          is the default.DRIVINGDISTANCE-Use distance as driven in an
          automobile.DRIVINGTIME-Use distance covered during a specified driving
          time in an
          automobile.TRUCKINGDISTANCE-Use distance as driven in a
          truck.TRUCKINGTIME-Use distance covered during a specified driving
          time in a
          truck.WALKINGDISTANCE-Use distance as walked along a
          street.WALKINGTIME-Use distance covered during a specified walking
          time.
      distances (Double):
          A list of double values that defines the search distance (for
          straight-line and distance-based travel modes) or time (for time-based
          travel modes). You can enter a single distance value or multiple
          values. Features that are within (or equal to) the distances you enter
          will be summarized. The units of the distance values is supplied by
          the units parameter.
      units (String):
          If the near type is straight-line or a distance-based travel mode,
          this is the linear unit to be used with the distance values specified
          in distances. Valid options include meters, kilometers, feet, yards,
          and miles.If the near type is a time-based travel mode, values include
          seconds,
          minutes, and hours.MILES-MilesFEET-FeetKILOMETERS-KilometersMETERS-Met
          ersYARDS-YardsSECON
          DS-SecondsMINUTES-MinutesHOURS-Hours
      timeOfDay {Date}:
          Specify whether travel times should consider traffic conditions. To
          use traffic in the analysis, you must set the near type to a travel-
          time-based mode. The time of day value represents the time at which
          travel begins, or departs, from the input points.Two kinds of traffic
          are supported: typical and live. Typical traffic
          references travel speeds that are made up of historical averages for
          each 5-minute interval spanning a week. Live traffic retrieves speeds
          from a traffic feed that processes phone probe records, sensors, and
          other data sources to record actual travel speeds and predict speeds
          for the near future. To ensure the task uses typical traffic in
          locations where it
          is available, choose a time and day of the week and convert the day of
          the week to one of the following dates from 1990:Although the dates
          representing days of the week are from 1990, typical traffic is
          calculated from recent traffic trends-usually over the last several
          months.
          Monday-1/1/1990Tuesday-1/2/1990Wednesday-1/3/1990Thursday-1/4/1990Frid
          ay-1/5/1990Saturday-1/6/1990Sunday-1/7/1990To use live traffic when
          and where it is available, choose a date and
          time within 12 hours of the current time. Esri saves live traffic data
          for 12 hours and references predictive data extending 12 hours into
          the future. If the time and date you specify for this parameter is
          outside the 24-hour time window, or the travel time in the analysis
          continues past the predictive data window, the task falls back to
          typical traffic speeds.
      timeZoneForTimeOfDay {String}:
          Specify the time zone or zones of the chosen time of day. There are
          two options: GeoLocal (default) and UTC.GEOLOCAL-The time of day value
          refers to the time zone or zones in
          which the input points are located. This option causes the analysis to
          have rolling start times across time zones. This is the
          default.UTC-The time of day value refers to Coordinated Universal Time
          (UTC).
          The start times for all points are simultaneous, regardless of time
          zones.
      returnBoundaries {Boolean}:
          Specifies whether the input geometries will be returned or the
          straight-line or travel mode buffer geometry.RETURN_BOUNDARIES-The
          output layer will contain areas defined by the
          specified near type. For example, if using a straight-line distance of
          5 miles, the output will contain areas with a 5-mile radius around the
          input nearby layer features. This is the default.RETURN_INPUT-The
          output layer will contain the same features as the
          input nearby layer.
      sumShape {Boolean}:
          Calculate statistics based on the shape of the input summary features,
          such as the length of lines or areas of polygons of the summary
          features within each polygon in the input summary
          layer.ADD_SHAPE_SUM-Calculate the shape summary attributes. This is
          the
          default.NO_SHAPE_SUM-Do not calculate the shape summary attributes.
      shapeUnits {String}:
          If summarizing the shape of the nearby features, specify the units of
          the shape summary.When the input summary features are polygons, the
          valid options are
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
          This is a field from the input summary features you can use to
          calculate statistics separately for each unique attribute value. For
          example, suppose the input summary features contain point locations of
          businesses that store hazardous materials, and one of the fields
          iscontaining codes that describe the type of hazardous material
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
          nearby feature.NO_PERCENT-Do not add percentage fields. This is the
          default.ADD_PERCENT-Add percentage fields.

        """