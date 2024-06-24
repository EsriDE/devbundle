# Generated documentation for module arcpy.stats


class OrdinaryLeastSquares(object):
    """
    Performs global Ordinary Least Squares (OLS) linear regression to generate predictions or to model a dependent variable in terms of its relationships to a set of explanatory variables.
    """

    @property
    def description(self) -> str:
        return """

        OrdinaryLeastSquares_stats(Input_Feature_Class, Unique_ID_Field, Output_Feature_Class, Dependent_Variable, Explanatory_Variables;Explanatory_Variables..., {Coefficient_Output_Table}, {Diagnostic_Output_Table}, {Output_Report_File})

        Performs global Ordinary Least Squares (OLS) linear regression to
        generate predictions or to model a dependent variable in terms of its
        relationships to a set of explanatory variables.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing the dependent and independent variables
          for analysis.
      Unique_ID_Field (Field):
          An integer field containing a different value for every
          feature in the. Input Feature Class
      Dependent_Variable (Field):
          The numeric field containing values for what you are trying to model.
      Explanatory_Variables (Field):
          A list of fields representing explanatory variables in your regression
          model.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class that will receive dependent variable
          estimates and residuals.
      Coefficient_Output_Table {Table}:
          The full path to an optional table that will receive model
          coefficients, standardized coefficients, standard errors, and
          probabilities for each explanatory variable.
      Diagnostic_Output_Table {Table}:
          The full path to an optional table that will receive model summary
          diagnostics.
      Output_Report_File {File}:
          The path to the optional PDF file the tool will create. This report
          file includes model diagnostics, graphs, and notes to help you
          interpret the OLS results.

        """