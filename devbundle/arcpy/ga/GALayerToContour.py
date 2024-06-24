# Generated documentation for module arcpy.ga


class GALayerToContour(object):
    """
    Creates a feature class of contours from a geostatistical layer. The output feature class can be either a line feature class of contour lines or a polygon feature class of filled contours.
    """

    @property
    def description(self) -> str:
        return """

        GALayerToContour_ga(in_geostat_layer, contour_type, out_feature_class, {contour_quality}, {classification_type}, {classes_count}, {classes_breaks;classes_breaks...}, {out_elevation})

        Creates a feature class of contours from a geostatistical layer. The
        output feature class can be either a line feature class of contour
        lines or a polygon feature class of filled contours.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      contour_type (String):
          Type of contour to represent the geostatistical layer.CONTOUR-The
          contour or isoline representation of the geostatistical
          layer. Displays the lines in either draft or presentation
          quality.FILLED_CONTOUR-The polygon representation of the
          geostatistical layer.
          It assumes for the graphical display that the values between contour
          lines are the same for all locations within the polygon. Displays the
          lines in either draft or presentation quality.SAME_AS_LAYER-Use the
          current renderer of the input geostatistical
          layer.
      contour_quality {String}:
          Determines the smoothness of contour line representation.DRAFT-The
          default Draft quality presents a generalized version of
          isolines for faster display.PRESENTATION-The Presentation option
          ensures more detailed isolines
          for the output feature class.
      classification_type {String}:
          Specifies how the contour breaks will be
          calculated.GEOMETRIC_INTERVAL-Contour breaks are calculated based on
          geometric
          intervals.EQUAL_INTERVAL-Contour breaks are calculated based on equal
          intervals.QUANTILE-Contour breaks are calculated from quantiles of the
          input
          data.MANUAL-Specify your own break values.
      classes_count {Long}:
          Specify the number of classes in the output feature class.If
          contour_type is set to output filled contour polygons, the number
          of polygons created will equal the value specified in this parameter.
          If it is set to output contour polylines, the number of polylines will
          be one less than the value specified in this parameter (because N
          class intervals define N-1 contour break values).This parameter does
          not apply if the classification_type is set to
          Manual.
      classes_breaks {Double}:
          The list of break values if the classification_type is set to Manual.
          The values should be passed as a list, and the values can be in any
          order.For contour output, these are the values of the contour
          lines.For
          filled contour, these are the upper limits of each class interval.
          Note that if the largest break value is less than the maximum of the
          geostatistical layer, the output feature class will not fill up the
          entire rectangular extent; all locations with predicted values above
          the largest break will not receive filled contours.
      out_elevation {Linear Unit}:
          For 3D interpolation models, you can export contours at any elevation.
          Use this parameter to specify the elevation that you want to export.
          If left empty, the elevation will be inherited from the input layer.
          The units will default to the same units of the input layer.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class will either be a polyline or a polygon,
          depending on the selected contour type.

        """