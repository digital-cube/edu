LESSON 2
========
The topics discussed were:
- Defining an HTML Table
- Colspan and Rowspan in html
- Table performance in css
- DIV, CLASS and ID
- Example
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

Tables performance
------------------

- Table borders

The example below specifies a black border for table, th and td elements:
```html
table, th, td {
                        border: 1px solid black;
                    }
```
```html
<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>TABELA</title>
                <style t="text/css">
                    table, th, td {
                        border: 1px solid black;
                    }
                </style>
            </head>
            <body>
            <table>
                <tr>
                <th>ZIKA</th>
                <td> I love tables</td>
                <td> I love tables</td>
                <td> I love tables</td>
                </tr>
                <tr>
                <th>PERA</th>
                <td> I love tables</td>
                <td> I love tables</td>
                <td> I love tables</td>
                </tr>
            </table>
            </body>
            </html>
```
[For more examples go to the link] (http://www.w3schools.com/css/css_table.asp "W3schools")


DIV
---
The DIV tag defines a division or a section of the page.
Div give us structure to our page. The div tag is used to group block-elements to format them with CSS.

CLASS
-----
The (.class) selector selects elements with a specific class attribute.
To select elements with a specific class, write a period (.) character, followed by the name of the class.
You can use the same class on multiple elements, or you can use multiple classes on the same element.
Any styling information that needs to be applied to multiple objects on a page should be done with a class.

ID
--
Each element can have only one ID.
Each page can have only one element with that ID.

Difference between id and class?
Main difference is IDs are to be used only once in your html layout.Classes can be used multiple times.
Ids have priority over classes. So, if an element has a both id and class, the id will take over.

EXAMPLE
-------
``` html
<div class="mytable">

    <div class="mytable">

         <div class="myrow">

             <div class="mycell">
                 value 1
             </div>
             <div class="mycell">
                 value 2
             </div>

         </div>

         <div class="myrow">

             <div class="mycell">
                 value 1
             </div>
             <div class="mycell">
                 value 2
             </div>

         </div>

     </div>
```

``` css
.mytable {
    width:300px;
    display:table;
    border:1px solid red;
    padding:1em;
    border-collapse:separate;
    border-spacing:1em;
}

.myrow {
    display:table-row;
}

.mycell {
    display:table-cell;
    border:1px solid green;
    padding:1em;
}
```
Problem with margin property of table cells
-------------------------------------------

If you want to make space between table cells you can't use margin property because it's not
applicable to display: table-cell elements.
Only solution is to style parent DIV with border spacing property:

[From the MDN documentation:](https://developer.mozilla.org/en-US/docs/CSS/margin)
```html
    [The margin property] applies to all elements except elements with table
     display types other than table-caption, table and inline-table
```

- In CSS style you must write:
```html

table {
                border-collapse: separate;
                border-spacing: 10px 5px;
      }
```
The values for border-spacing are two length measurements. First value (horizontal) applies between columns,
the second measurement is applied between rows. If you provide one value, it will be used both horizontally and vertically.
