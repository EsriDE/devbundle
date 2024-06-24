# Generated documentation for module arcpy.ba


class ColorCodedLayer(object):
    """
    Creates multilevel, scale-dependent choropleth layers from a variable describing a business, demographic, consumer, or landscape characteristic.
    """

    @property
    def description(self) -> str:
        return """

        ColorCodedLayer_ba(classification_variable, out_layer_name, classification_method, number_of_classes, {area_of_interest}, {out_dataset_path}, {out_dataset_name})

        Creates multilevel, scale-dependent choropleth layers from a variable
        describing a business, demographic, consumer, or landscape
        characteristic.

     INPUTS:
      classification_variable (String):
          A variable that will display as a color-coded map.
      out_layer_name (String):
          The name of the color-coded layer that will be added to the map.
      classification_method (String):
          Specifies the method that will be used to calculate the class
          breaks.NATURAL_BREAKS-Natural breaks classes are based on natural
          groupings
          inherent in the data. Class breaks that best group similar values and
          that maximize the differences between classes will be identified. This
          is the default.QUANTILE-Each class will contain an equal number of
          features. A
          quantile classification is well suited to linearly distributed
          data.EQUAL_INTERVAL-The range of attribute values will be divided into
          equal-sized subranges. This allows you to specify the number of
          intervals, and will automatically determine the class breaks based on
          the value range.GEOMETRIC_INTERVAL-Class breaks will be created based
          on class
          intervals that have a geometric series. The geometric coefficient in
          this classifier can change once (to its inverse) to optimize the class
          ranges.AUTO-Classification methods will be automatically defined using
          the
          variable metadata. This presents the recommended thematic map style
          based on the data type.
      number_of_classes (String):
          The number of data classification breaks that will appear on the map.
          The default value is 5.
      area_of_interest {Feature Layer}:
          A feature layer that will be used to determine the geographic extent
          of the analysis.
      out_dataset_path {Workspace}:
          The geodatabase in which the output feature dataset will be created.
      out_dataset_name {String}:
          The name of the feature dataset in the output geodatabase in which the
          color-coded layer feature classes will be created.

        """