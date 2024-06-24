# Generated documentation for module arcpy.aviation


class UnifiedFacilitiesCriteria(object):
    """
    Creates obstruction identification surfaces (OIS) based on the Unified Facilities Criteria (UFC) 3-260-01 that is prescribed by MIL-STD 3007. These surfaces provide planning, design, construction, sustainment, restoration, and modernization criteria for the United States Department of Defense. Surfaces are created as polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        UnifiedFacilitiesCriteria_aviation(in_runway_features, target_ois_features, in_wing_type, in_service_type, in_runway_class, in_flight_rule, {highend_clear_way_length}, {lowend_clear_way_length}, {airport_elevation}, {custom_json_file}, {airport_control_point_feature_class})

        Creates obstruction identification surfaces (OIS) based on the Unified
        Facilities Criteria (UFC) 3-260-01 that is prescribed by MIL-STD 3007.
        These surfaces provide planning, design, construction, sustainment,
        restoration, and modernization criteria for the United States
        Department of Defense. Surfaces are created as polygon or multipatch
        features.

     INPUTS:
      in_runway_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target_ois_features (Feature Layer):
          The existing output feature class that will contain the generated UFC
          surfaces.
      in_wing_type (String):
          Specifies the wing type of the aircraft.FIXED-The wing type is
          fixed.ROTARY-The wing type is rotary.If you specify ROTARY, the
          in_runway_class parameter will default to
          the CLASS_A option without affecting the surface generation.
      in_service_type (String):
          Specifies the type of military service.AIRFORCE-The service type is
          Air Force.ARMY-The service type is
          Army.NAVY-The service type is Navy.MARINECORPS-The service type is
          Marine Corps.
      in_runway_class (String):
          Specifies the runway class. Runways are classified as either Class A
          or Class B based on aircraft type.CLASS_A-The runway classification is
          Class A.CLASS_B-The runway
          classification is Class B.
      in_flight_rule (String):
          Specifies the flight rule. These are the rules that govern the
          procedures for conducting flight, either instrument or under visual
          conditions.INSTRUMENT-The flight rule is instrument flight
          condition.VISUAL-The
          flight rule is visual flight condition.
      highend_clear_way_length {Double}:
          The length of the area at the high end of the runway. The unit of
          measurement is based on the input runway features.
      lowend_clear_way_length {Double}:
          The length of the area at the low end of the runway. The unit of
          measurement is based on the input runway features.
      airport_elevation {Double}:
          The highest elevation on any of the runways of the airport.
          Provide the value in the vertical coordinate system linear units of
          the target feature class. If no value is provided, the highest point
          of theparameter value will be used. Input Runway Features
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      airport_control_point_feature_class {Feature Layer}:
          The point features containing anfeature, displaced threshold
          features, or both. Values provided for theparameter will take
          precedence over these point features. Airport ElevationAirport
          Elevation

        """