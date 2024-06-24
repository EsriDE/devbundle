# Generated documentation for module arcpy.management


class CalculateGeometryAttributes(object):
    """
    Adds information to a feature's attribute fields representing the spatial or geometric characteristics and location of each feature, such as length or area and x-, y-, z-coordinates, and m-values.
    """

    @property
    def description(self) -> str:
        return """

        CalculateGeometryAttributes_management(in_features, geometry_property;geometry_property..., {length_unit}, {area_unit}, {coordinate_system}, {coordinate_format})

        Adds information to a feature's attribute fields representing the
        spatial or geometric characteristics and location of each feature,
        such as length or area and x-, y-, z-coordinates, and m-values.

     INPUTS:
      in_features (Feature Layer):
          The features with a field that will be updated with geometry
          calculations.
      geometry_property (Value Table):
          The fields in which the specified geometry properties will be
          calculated.You can select an existing field or provide a new field
          name. If a new
          field name is provided, the field type is determined by the type of
          values that are written to the field. Count attributes are written to
          long integer fields; area, length, and x-, y-, z-coordinate, and
          m-value attributes are written to double fields; and coordinate
          notations such as Degrees Minutes Seconds or MGRS are written to text
          fields.Unless otherwise noted, area and length properties are planar
          measurements using 2D Cartesian mathematics.AREA-An attribute will be
          added to store the area of each polygon
          feature.AREA_GEODESIC-An attribute will be added to store the shape-
          preserving
          geodesic area of each polygon feature.CENTROID_X-An attribute will be
          added to store the centroid
          x-coordinate of each feature.CENTROID_Y-An attribute will be added to
          store the centroid
          y-coordinate of each feature.CENTROID_Z-An attribute will be added to
          store the centroid
          z-coordinate of each feature.CENTROID_M-An attribute will be added to
          store the centroid m-value of
          each feature.INSIDE_X-An attribute will be added to store the
          x-coordinate of a
          central point inside or on each feature. This point is the same as the
          centroid if the centroid is inside the feature; otherwise, it is an
          inner label point.INSIDE_Y-An attribute will be added to store the
          y-coordinate of a
          central point inside or on each feature. This point is the same as the
          centroid if the centroid is inside the feature; otherwise, it is an
          inner label point.INSIDE_Z-An attribute will be added to store the
          z-coordinate of a
          central point inside or on each feature. This point is the same as the
          centroid if the centroid is inside the feature; otherwise, it is an
          inner label point.INSIDE_M-An attribute will be added to store the
          m-value of a central
          point inside or on each feature. This point is the same as the
          centroid if the centroid is inside the feature; otherwise, it is an
          inner label point.CURVE_COUNT-An attribute will be added to store the
          number of curves
          in each feature. Curves include elliptical arcs, circular arcs, and
          Bezier curves.HOLE_COUNT-An attribute will be added to store the
          number of interior
          holes within each polygon feature.EXTENT_MIN_X-An attribute will be
          added to store the minimum
          x-coordinate of each feature's extent.EXTENT_MIN_Y-An attribute will
          be added to store the minimum
          y-coordinate of each feature's extent.EXTENT_MIN_Z-An attribute will
          be added to store the minimum
          z-coordinate of each feature's extent.EXTENT_MAX_X-An attribute will
          be added to store the maximum
          x-coordinate of each feature's extent.EXTENT_MAX_Y-An attribute will
          be added to store the maximum
          y-coordinate of each feature's extent.EXTENT_MAX_Z-An attribute will
          be added to store the maximum
          z-coordinate of each feature's extent.LENGTH-An attribute will be
          added to store the length of each line
          feature.LENGTH_GEODESIC-An attribute will be added to store the shape-
          preserving geodesic length of each line feature.LENGTH_3D-An attribute
          will be added to store the 3D length of each
          line feature.LINE_BEARING-An attribute will be added to store the
          start-to-end
          bearing of each line feature. Values range from 0 to 360, with 0
          meaning north, 90 east, 180 south, 270 west, and so on.LINE_START_X-An
          attribute will be added to store the x-coordinate of
          the start point of each line feature.LINE_START_Y-An attribute will be
          added to store the y-coordinate of
          the start point of each line feature.LINE_START_Z-An attribute will be
          added to store the z-coordinate of
          the start point of each line feature.LINE_START_M-An attribute will be
          added to store the m-value of the
          start point of each line feature.LINE_END_X-An attribute will be added
          to store the x-coordinate of the
          end point of each line feature.LINE_END_Y-An attribute will be added
          to store the y-coordinate of the
          end point of each line feature.LINE_END_Z-An attribute will be added
          to store the z-coordinate of the
          end point of each line feature.LINE_END_M-An attribute will be added
          to store the m-value of the end
          point of each line feature.PART_COUNT-An attribute will be added to
          store the number of parts
          composing each feature.POINT_COUNT-An attribute will be added to store
          the number of points
          or vertices composing each feature.PERIMETER_LENGTH-An attribute will
          be added to store the length of the
          perimeter or border of each polygon
          feature.PERIMETER_LENGTH_GEODESIC-An attribute will be added to store
          the
          shape-preserving geodesic length of the perimeter or border of each
          polygon feature.POINT_X-An attribute will be added to store the
          x-coordinate of each
          point feature.POINT_Y-An attribute will be added to store the
          y-coordinate of each
          point feature.POINT_Z-An attribute will be added to store the
          z-coordinate of each
          point feature.POINT_M-An attribute will be added to store the m-value
          of each point
          feature.POINT_COORD_NOTATION-An attribute will be added to store the
          x- and
          y-coordinate of each point feature formatted as a specified coordinate
          notation.
      length_unit {String}:
          Specifies the unit that will be used to calculate
          length.KILOMETERS-The length unit will be kilometers.METERS-The length
          unit
          will be meters.MILES_INT-The length unit will be statute
          miles.NAUTICAL_MILES_INT-The length unit will be international
          nautical
          miles.YARDS_INT-The length unit will be international
          yards.FEET_INT-The length unit will be international feet.MILES_US-The
          length unit will be US survey miles.NAUTICAL_MILES-The length unit
          will be US survey nautical miles.YARDS-The length unit will be US
          survey yards.FEET_US-The length unit will be US survey feet.
      area_unit {String}:
          Specifies the unit that will be used to calculate
          area.SQUARE_KILOMETERS-The area unit will be square
          kilometers.HECTARES-The
          area unit will be hectares.SQUARE_METERS-The area unit will be square
          meters.SQUARE_MILES_INT-The area unit will be square statute
          miles.SQUARE_NAUTICAL_MILES-The area unit will be square international
          nautical miles.ACRES-The area unit will be international
          acres.SQUARE_YARDS-The area unit will be square international
          yards.SQUARE_FEET_INT-The area unit will be square international
          feet.SQUARE_MILES_US-The area unit will be square US survey
          miles.SQUARE_NAUTICAL_MILES_US-The area unit will be square US survey
          nautical miles.ACRES_US-The area unit will be US survey
          acres.SQUARE_YARDS_US-The area unit will be square US survey
          yards.SQUARE_FEET_US-The area unit will be square US survey feet.
      coordinate_system {Coordinate System}:
          The coordinate system in which the coordinates, length, and area will
          be calculated. The coordinate system of the input features is used by
          default.
      coordinate_format {String}:
          Specifies the coordinate format in which the x- and y-coordinates will
          be calculated. The coordinate format matching the input features'
          spatial reference units is used by default.Several coordinate formats,
          including Degrees Minutes Seconds, Degrees
          Decimal Minutes, and others, require the calculation to be performed
          in a text field.SAME_AS_INPUT-The input features' spatial reference
          units will be used
          for coordinate formatting. This is the default.DD-The coordinate
          format will be Decimal Degrees.DMS_DIR_LAST-The coordinate format will
          be Degrees Minutes Seconds
          with cardinal direction component at the end (DDD° MM' SSS.ss"
          <N|S|E|W>).DMS_DIR_FIRST-The coordinate format will be Degrees Minutes
          Seconds
          with cardinal direction component at the beginning (<N|S|E|W> DDD° MM'
          SSS.ss").DMS_POS_NEG-The coordinate format will be Degrees Minutes
          Seconds with
          positive or negative direction component at the beginning (<+|-> DDD°
          MM' SSS.ss").DMS_PACKED-The coordinate format will be Degrees Minutes
          Seconds
          packed into a single value with positive or negative direction
          component at the beginning (<+|-> DDD.MMSSSss).DDM_DIR_LAST-The
          coordinate format will be Degrees Decimal Minutes
          with cardinal direction component at the end (DDD° MM.mmm'
          <N|S|E|W>).DDM_DIR_FIRST-The coordinate format will be Degrees Decimal
          Minutes
          with cardinal direction component at the beginning (<N|S|E|W> DDD°
          MM.mmm').DDM_POS_NEG-The coordinate format will be Degrees Decimal
          Minutes with
          positive or negative direction component at the beginning (<+|-> DDD°
          MM.mmm').GARS-The coordinate format will be Global Area Reference
          System. The
          Global Area Reference System is based on latitude and longitude,
          dividing and subdividing the world into cells.GEOREF-The coordinate
          format will be World Geographic Reference
          System. The World Geographic Reference System is based on the
          geographic system of latitude and longitude, but using a simpler and
          more flexible notation.MGRS-The coordinate format will be Military
          Grid Reference System.USNG-The coordinate format will be United States
          National Grid.UTM-The coordinate format will be Universal Transverse
          Mercator.UTMNS-The coordinate format will be Universal Transverse
          Mercator with
          no spaces.

        """