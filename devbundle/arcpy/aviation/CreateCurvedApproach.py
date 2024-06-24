# Generated documentation for module arcpy.aviation


class CreateCurvedApproach(object):
    """
    Creates curved approach obstacle identification surfaces (OIS) based on the supported specifications in ArcGIS Aviation. These curved approach surfaces are based on an input flight path and the information in the selected specification, for example, ICAO Annex 15, FAA 18B and classification. This tool creates surfaces in existing polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        CreateCurvedApproach_aviation(in_runway_features, in_flightpath_features, target_ois_features, specification, runway_classification, {custom_json_file}, {threshold_offset})

        Creates curved approach obstacle identification surfaces (OIS) based
        on the supported specifications in ArcGIS Aviation. These curved
        approach surfaces are based on an input flight path and the
        information in the selected specification, for example, ICAO Annex 15,
        FAA 18B and classification. This tool creates surfaces in existing
        polygon or multipatch features.

     INPUTS:
      in_runway_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      in_flightpath_features (Feature Layer):
          The polyline features that define curved approaches to the specified
          runways, terminating at the runway centerline endpoint.
      target_ois_features (Feature Layer):
          The target feature class that will contain the generated OIS.
      specification (String):
          Specifies the approach surface specification.ETOD-The approach surface
          specification is ICAO Annex 15
          (ETOD).OLS-The approach surface specification is ICAO Annex 14
          (OLS).FAR77-The approach surface specification is FAA regulations part
          77
          (FAR77).18B-The approach surface specification is FAA Advisory
          circular
          150/5300_18B (18B).13SURFACES-The approach surface specification is
          FAA Advisory circular
          150/5300_13.
      runway_classification (String):
          The runway classification of the approach surface.The specification
          parameter value will determine the available options
          for this parameter.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      threshold_offset {Double}:
          A positive distance value that will be used to offset the generated
          approach surface outward from the runway end. The offset will be
          applied in the units of the input.

        """