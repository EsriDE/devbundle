# Generated documentation for module arcpy.ba


class SetCriteriaProperties(object):
    """
    Define parameters for criteria.
    """

    @property
    def description(self) -> str:
        return """

        SetCriteriaProperties_ba(in_analysis_layer, criteria_properties;criteria_properties...)

        Define parameters for criteria.

     INPUTS:
      in_analysis_layer (Feature Layer):
          The Suitability Analysis layer that will be used in the analysis.
      criteria_properties (Value Table):
          The input features that will be used to set up your criteria
          properties.criterion-The field, point, or variable that will be used
          to calculate
          your suitability score.title-The name of your criteria.weight-The
          influence a criteria value has on the overall suitability
          score. The number must be greater than or equal to 0.
          influence-Can be positive, inverse, or ideal. An example of a
          positive influence is as follows: You want a site to score higher if
          it has a greater number of households holding graduate or professional
          degrees. An example of an inverse influence is as follows: A lower
          median home value is more desirable as it is indicative of greater
          home affordability. An example of an ideal influence would be a search
          for areas within a range of values. POSITIVE-The higher the
          criteria value, the higher the suitability
          score.INVERSE-The lower the criteria value, the higher the suitability
          score.IDEAL-The closer to the ideal value, the higher the
          score.ideal_value-The closer the criteria value is to the ideal_value,
          the
          higher the suitability score.minimum_value-A numeric value that sets a
          hard limit for the criteria
          lower bound.maximum_value-A numeric value that sets a hard limit for
          the criteria
          upper bound.enabled-Check to include the criteria in the final
          suitability score.

        """