# Generated documentation for module arcpy.parcel


class AnalyzeParcelsByLeastSquaresAdjustment(object):
    """
    Analyzes the parcel fabric measurement network by running a least- squares adjustment on the input parcels. A least-squares adjustment is a mathematical procedure that uses statistical analysis to estimate the most likely coordinates for connected points in a measurement network. A least-squares adjustment can be run on the parcel fabric to evaluate and improve spatial accuracy of parcel corner point locations.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeParcelsByLeastSquaresAdjustment_parcel(in_parcel_fabric, analysis_type, {convergence_tolerance})

        Analyzes the parcel fabric measurement network by running a least-
        squares adjustment on the input parcels. A least-squares adjustment is
        a mathematical procedure that uses statistical analysis to estimate
        the most likely coordinates for connected points in a measurement
        network. A least-squares adjustment can be run on the parcel fabric to
        evaluate and improve spatial accuracy of parcel corner point
        locations.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The input parcel fabric to be analyzed by least-squares adjustment.
      analysis_type (String):
          Specifies the type of least-squares analysis that will be used in the
          adjustment.CONSISTENCY_CHECK-A free-network least-squares adjustment
          will be run
          to check dimensions on parcel lines for inconsistencies and mistakes.
          Fixed or weighted control points will not be used by the
          adjustment.WEIGHTED_LEAST_SQUARES-A weighted least-squares adjustment
          will be run
          to compute updated coordinates for parcel points. The parcels being
          adjusted should connect to at least two fixed or weighted control
          points.
      convergence_tolerance {Linear Unit}:
          The tolerance representing the maximum coordinate shift expected after
          iterating the least-squares adjustment. A least-squares adjustment is
          run repeatedly (in iterations) until the solution converges. The
          solution is considered converged when maximum coordinate shift
          encountered becomes less than the specified convergence tolerance. The
          default value is 0.05 meters.

        """