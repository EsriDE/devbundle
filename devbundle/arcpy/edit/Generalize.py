# Generated documentation for module arcpy.edit


class Generalize(object):
    """
    Simplifies the input features using a specified maximum offset tolerance. The output features will contain a subset of the original input vertices.
    """

    @property
    def description(self) -> str:
        return """

        Generalize_edit(in_features, {tolerance})

        Simplifies the input features using a specified maximum offset
        tolerance. The output features will contain a subset of the original
        input vertices.

     INPUTS:
      in_features (Feature Layer):
          The polygon or line features to be generalized.
      tolerance {Linear Unit}:
          The tolerance sets the maximum allowable offset, which will determine
          the degree of simplification. This value limits the distance the
          output geometry can differ from the input geometry. You can specify a
          preferred unit of measurement. The default is the feature unit.

        """