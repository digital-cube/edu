LESSON 2
========
The topics disscused were:
- Defining an HTML Table
- Colspan and Rowspan in html
- Problem with margin property of table cells

Defining an HTML Table
----------------------
- HTML table is defined with the **\<table\>** tag
- Table header is defined with the **\<th\>** tag
- Table row is defined with the **\<tr\>** tag
- Table column is defined with the **\<td\>** (table data/cell)

Colspan and Rowspan in html
----------------------------
- Colspan attribute defines the number of **columns** a cell should span (merge cells to the right)
- Rowspan attribute specifies the number of **rows** a cell should span (merge cells down)

Problem with margin property of table cells
-------------------------------------------
- In CSS style you must wrote:
```html

table {
                border-collapse: separate;
                border-spacing: 10px 5px;
      }
```
The values for border-spacing are two length measurements. First value (horizontal) applies between columns,
the second measurement is applied between rows. If you provide one value, it will be used both horizontally and vertically