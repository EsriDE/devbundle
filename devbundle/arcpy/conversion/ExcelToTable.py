# Generated documentation for module arcpy.conversion


class ExcelToTable(object):
    """
    Converts Microsoft Excel files into a table.
    """

    @property
    def description(self) -> str:
        return """

        ExcelToTable_conversion(Input_Excel_File, Output_Table, {Sheet}, {field_names_row}, {cell_range})

        Converts Microsoft Excel files into a table.

     INPUTS:
      Input_Excel_File (File):
          The Excel file to convert.
      Sheet {String}:
          The name of the particular sheet in the Excel file to import. If
          unspecified, the first sheet in the workbook will be used.
      field_names_row {Long}:
          The row in the Excel sheet that contains values to be used as field
          names. The default value is 1.The row specified will be skipped when
          converting records to the
          output table. To avoid using any row's values as field names,
          set this
          parameter to 0, which will name the output fields using the column
          letter (for example,,,). COL_ACOL_BCOL_C        If a cell in a
          particular column is empty, the output field
          name will be based on the column letter. For example, if the input has
          three columns, and the row contains "city", "", and "country" in
          columns A, B, and C respectively, the output table's field names will
          be,, and. cityCOL_Bcountry
      cell_range {String}:
          The cell range to include.A cell is the intersection of a row and a
          column. Columns are
          identified by letters (A, B, C, D), and rows are identified by numbers
          (1, 2, 3, 4). Each cell has an address based on its column and row.
          For example, the cell B9 is the intersection of column B and row 9.A
          cell range defines a rectangle using the upper left cell and lower
          right cell, separated by a colon (:). Cell ranges are inclusive, so a
          range of A2:C10 will include all values in columns A through C and all
          values in rows 2 through 10.The output field names are derived from
          cell values in row 1,
          regardless of the rows specified in the cell range. For example, if
          the cell range specified is B2:D10, the field names will be based on
          the values in cells B1, C1, and D1. The following are examples
          of valid cell ranges:
          A2:C10-The values in columns A through C, from row 2 through
          10B3:B40-The values in column B, from rows 3 through 40D5:X5-The
          values in columns D through X, for row 5E200:ALM20000-The values in
          columns E through ALM (1000th column),
          from row 200 through 20000        The following are examples of
          invalid cell ranges:
          A20:C10-The first cell cannot be lower (have a larger row number) than
          the second cell.Z3:B5-The second cell cannot be to the right (have a
          larger column
          letter) of the first cell.A5:G-Both cells must have a valid cell
          identifier: a letter and a
          number.

     OUTPUTS:
      Output_Table (Table):
          The output table.

        """