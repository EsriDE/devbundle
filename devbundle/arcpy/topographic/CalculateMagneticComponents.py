# Generated documentation for module arcpy.topographic


class CalculateMagneticComponents(object):
    """
    Calculates the magnetic field at point locations for given date and altitude.
    """

    @property
    def description(self) -> str:
        return """

        CalculateMagneticComponents_topographic(in_features, altitude, date, magnetic_component;magnetic_component...)

        Calculates the magnetic field at point locations for given date and
        altitude.

     INPUTS:
      in_features (Feature Layer):
          The point features for which magnetic field values will be calculated.
      altitude (Linear Unit):
          The elevation of the in_features value including the linear unit. Do
          not use decimal degrees or unknown units. The default is 0 meters.
      date (Date):
          The date for which magnetic field values will be calculated. The date
          must be valid for the specified World Magnetic Model. The format must
          use two digits for the month, two digits for the day, and four digits
          for the year. The default is the system current date.
      magnetic_component (Value Table):
          The magnetic component that will be calculated and the field to which
          the values will be written. Component-The magnetic component
          to calculate.
          DECLINATION-The angle between magnetic north and true north. This
          value varies by location on the globe.ANNUAL_DRIFT-The annual rate of
          change in magnetic declination. This
          value varies by location on the globe.INCLINATION-The angle between a
          compass needle and the plane of the
          horizon. Inclination is also known as magnetic dip or the dip of the
          compass needle. This value varies by latitude.HORIZONTAL-This value is
          calculated using north and east components.
          Horizontal is also known as Horizontal intensity, or H. This value
          varies by location on the globe.EAST_COMPONENT-The easterly intensity
          of the geomagnetic field. East
          component is also known as Y. This value varies by location on the
          globe.NORTH_COMPONENT-The northerly intensity of the geomagnetic
          field.
          North component is also known as X. This value varies by location on
          the globe.VERTICAL_INTENSITY-The vertical intensity of the geomagnetic
          field.
          Vertical intensity is also known as Z. This value varies by location
          on the globe.TOTAL_INTENSITY-This value is calculated using horizontal
          and vertical
          components. Total intensity is also known as F. This value varies by
          location on the globe.GRID_VARIATION-The angle between magnetic north
          and grid north. You
          must use the Lambert conformal conic projected coordinate system in
          the map frame, in the geoprocessing environment, or in the input point
          data.Field-The field to which calculated results will be written.

        """