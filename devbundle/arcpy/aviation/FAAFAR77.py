# Generated documentation for module arcpy.aviation


class FAAFAR77(object):
    """
    Creates obstruction identification surfaces (OIS) based on the FAA Part 77 specification. This regulation establishes standards and notification requirements for objects affecting navigable airspace. The type, function, and dimension of a surface differ by its runway classification. This tool creates surfaces as a polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        FAAFAR77_aviation(in_features, target, high_runway_end_type, low_runway_end_type, {specially_prepared_hard_surface_runway}, {highend_clear_way_length}, {lowend_clear_way_length}, {airport_elevation}, {include_merged_surface}, {custom_json_file}, {airport_control_point_feature_class})

        Creates obstruction identification surfaces (OIS) based on the FAA
        Part 77 specification. This regulation establishes standards and
        notification requirements for objects affecting navigable airspace.
        The type, function, and dimension of a surface differ by its runway
        classification. This tool creates surfaces as a polygon or multipatch
        features.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The target feature class that will contain the generated OIS.
      high_runway_end_type (String):
          Specifies the classification of the high end of the runway.CONSTRUCTIO
          N_OR_ALTERATION_ON_AN_AIRPORT_WITH_LONGEST_RUNWAY_MORE_THAN
          _3200_FEET-Construction on or alteration to a runway longer than 3,200
          feet with an imaginary surface that extends outward 20,000 feet and
          has a slope that does not exceed 100 to 1.CONSTRUCTION_OR_ALTERATION_O
          N_AN_AIRPORT_WITH_LONGEST_RUNWAY_LESS_THAN
          _3200_FEET-Construction on or alteration to a runway less than 3,200
          feet long with an imaginary surface that extends outward 10,000 feet
          and has a slope that does not exceed 50 to
          1.CONSTRUCTION_OR_ALTERATION_ON_A_HELIPORT-Construction on or
          alteration
          to a heliport landing and takeoff area with an imaginary surface that
          extends outward 5,000 feet and has a slope that does not exceed 25 to
          1.MILITARY_AIRPORT-Military airport runways are operated by an armed
          force of the United States. Primary surfaces are the same length as
          the runway. Primary surface width is 2,000 feet. Clear zone surface
          length is 1,000 feet, and width is the same as the primary surface.
          The approach clearance surface starts 200 feet beyond each end of the
          primary surface and extends for 50,000 feet. Approach surface width
          matches the primary surface width at the runway end but flares to a
          width of 16,000 feet at an elevation of 50,000 feet. Approach
          clearance surface slope is 50 to 1 to an elevation of 500 feet above
          airport elevation. It then rises horizontally to 50,000 feet.
          Transitional surface slope is 7 to 1 outward and upward at right
          angles to the runway centerline. See section 77.28 in the FAR Part 77
          specification for more information.NONPRECISION_INSTRUMENT_RUNWAY_GREA
          TER_THAN_(>)_3/4_MILE_VISIBILITY-A
          runway with a nonprecision instrument approach procedure that allows
          for landing in visibility conditions greater than three-quarters of a
          mile.NONPRECISION_INSTRUMENT_RUNWAY_LESS_THAN_(<)_3/4_MILE_VISIBILITY-
          A
          runway with a nonprecision instrument approach procedure that allows
          for landing in visibility conditions less than three-quarters of a
          mile.PRECISION_INSTRUMENT_RUNWAY-A runway that uses Instrument Landing
          System (ILS) or Precision Approach Radar (PAR) for approach
          procedures.UTILITY_RUNWAY_VISUAL_APPROACH-A runway built for propeller
          aircraft
          not exceeding 12,500 pounds gross weight. Aircraft using the runway
          use visual approach
          procedures.UTILITY_RUNWAY_NON_PRECISION_INSTRUMENT_APPROACH-A runway
          built for
          propeller aircraft not exceeding 12,500 pounds gross weight. The
          runway has an instrument approach procedure that uses air navigation
          facilities with horizontal guidance. It can also have area-type
          navigation equipment with approved nonprecision instrument approach
          procedures.VISUAL_RUNWAY_VISUAL_APPROACH-A runway that supports only
          visual
          approach procedures.
      low_runway_end_type (String):
          Specifies the classification of the low end of the
          runway.SAME_AS_HIGH_RUNWAY_END_CLASSIFICATION-No low runway end
          type.NONPRECI
          SION_INSTRUMENT_RUNWAY_GREATER_THAN_(>)_3/4_MILE_VISIBILITY-A
          runway with a nonprecision instrument approach procedure that allows
          for landing in visibility conditions greater than three-quarters of a
          mile.NONPRECISION_INSTRUMENT_RUNWAY_LESS_THAN_(<)_3/4_MILE_VISIBILITY-
          A
          runway with a nonprecision instrument approach procedure that allows
          for landing in visibility conditions less than three-quarters of a
          mile.PRECISION_INSTRUMENT_RUNWAY-A runway that uses Instrument Landing
          System (ILS) or Precision Approach Radar (PAR) for approach
          procedures.UTILITY_RUNWAY_VISUAL_APPROACH-A runway built for propeller
          aircraft
          not exceeding 12,500 pounds gross weight. Aircraft using the runway
          use visual approach
          procedures.UTILITY_RUNWAY_NON_PRECISION_INSTRUMENT_APPROACH-A runway
          built for
          propeller aircraft not exceeding 12,500 pounds gross weight. The
          runway has an instrument approach procedure that uses air navigation
          facilities with horizontal guidance. It can also have area-type
          navigation equipment with approved nonprecision instrument approach
          procedures.VISUAL_RUNWAY_VISUAL_APPROACH-A runway that supports only
          visual
          approach procedures.
      specially_prepared_hard_surface_runway {Boolean}:
          Specifies whether the runway has a specially prepared hard surface. A
          specially prepared hard surface indicates that the primary surface
          extends 200 feet beyond each end of the
          runway.SPECIALLY_PREPARED_HARD_SURFACE_RUNWAY-The runway has a
          specially
          prepared hard surface. This is the
          default.NON_SPECIALLY_PREPARED_HARD_SURFACE_RUNWAY-The runway does not
          have a
          specially prepared hard surface.
      highend_clear_way_length {Double}:
          The length of the area at the high end of the runway. The unit of
          measurement is based on the input runway features.
      lowend_clear_way_length {Double}:
          The length of the area at the low end of the runway. The unit of
          measurement is based on the input runway features.
      airport_elevation {Double}:
          The highest elevation on any of the runways of the airport.
          The value should be in the vertical coordinate system linear units of
          the target feature class. If no value is provided, the highest point
          from theparameter value will be used. Input Runway Features
      include_merged_surface {Boolean}:
          Specifies whether merged horizontal and conical surfaces will be
          included in the OIS in addition to the regular
          surfaces.INCLUDE_MERGED_SURFACE-Merged surfaces will be included in
          the OIS
          output. This is the default.NOT_INCLUDE_MERGED_SURFACE-Merged surfaces
          will not be included in the
          OIS output.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      airport_control_point_feature_class {Feature Layer}:
          The point features containing anfeature, displaced threshold
          features, or both. Values provided for theparameter will take
          precedence over these point features. Airport ElevationAirport
          Elevation

        """