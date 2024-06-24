# Generated documentation for module arcpy.conversion


class AddCADFields(object):
    """
    Adds several reserved CAD fields in one step. Fields created by this tool are used by the Export To CAD tool to generate CAD entities with specific properties. After executing this tool, you must calculate or type the appropriate field values.
    """

    @property
    def description(self) -> str:
        return """

        AddCADFields_conversion(input_table, Entities, {LayerProps}, {TextProps}, {DocProps}, {XDataProps})

        Adds several reserved CAD fields in one step. Fields created by this
        tool are used by the Export To CAD tool to generate CAD entities with
        specific properties. After executing this tool, you must calculate or
        type the appropriate field values.

     INPUTS:
      input_table (Table View):
          Input table, feature class, or shapefile that will have the CAD-
          specific fields added to it
      Entities (Boolean):
          Adds the list of CAD-specific Entity property fields to the input
          tableADD_ENTITY_PROPERTIES-Adds the list of CAD-specific Entity
          property
          fields to the input tableNO_ENTITY_PROPERTIES-Does not add the list of
          CAD-specific Entity
          property fields to the input table
      LayerProps {Boolean}:
          Adds the list of CAD-specific Layer property fields to the input
          tableADD_LAYER_PROPERTIES-Adds the list of CAD-specific Layer property
          fields to the input tableNO_LAYER_PROPERTIES-Does not add the list of
          CAD-specific Layer
          property fields to the input table
      TextProps {Boolean}:
          Adds the list of CAD-specific Text property fields to the input
          tableADD_TEXT_PROPERTIES-Adds the list of CAD-specific Text property
          fields
          to the input tableNO_TEXT_PROPERTIES-Does not add the list of CAD-
          specific Text property
          fields to the input table
      DocProps {Boolean}:
          Adds the list of CAD-specific Document property fields to the input
          tableADD_DOCUMENT_PROPERTIES-Adds the list of CAD-specific Document
          property fields to the input tableNO_DOCUMENT_PROPERTIES-Does not add
          the list of CAD-specific Document
          property fields to the input table
      XDataProps {Boolean}:
          Adds the list of CAD-specific XData property fields to the input
          tableADD_XDATA_PROPERTIES-Adds the list of CAD-specific XData property
          fields to the input tableNO_XDATA_PROPERTIES-Does not add the list of
          CAD-specific XData
          property fields to the input table

        """