LESSON 1
========

The topics disscused were:
- CSS rule priorities
- CSS reset
- CSS units (px, em, %, pt)
- Collapsing margins (misc. Display, float, overflow and clear properties).
- CSS calc() function
- Size of viewport( misc. wrapper element in HTML markup)

CSS rule priorities
-------------------

When you are defining styles in your project, some rules apply:
- When styles overlap in the same element, only the last style is visible,
- Style from parent is inherited to child
- Rules of priorities are as follow : Script < !important < Element attribute < Class attribute < ID attribute

CSS reset
---------

CSS reset is a short set of CSS rules that resets the styling of all HTML elements. Main purpose of this is to maintain the look of website same in every browser by making common base.

CSS units(px, em, %, pt)
------------------------

There is four different units by which you can measure size of your elements as it's displayed in the web browser:

- Pixels (px): One pixel is equal to one dot on the computer screen.
- EMs : Em is relative unit that is used in web. Em is equal to the current font-size(if font-size is 12pt 1em =12pt).Ems are scalabile.
- Points (pt) : Similar to pixel, but one point is equal to 1/72 of an inch.
- Percent (%) : Similar to ems, current font size is equal to 100%.

Colapsing Margins (misc. Display, float, overflow and clear properties)
-----------------------------------------------------------------------

Before adresing Colapsing margins, there are some important properties to be avare of:

- Display property : For controlling layout. Elements can be usually block or inline. Block-level element starts on a new line and stretches to the left and right. Common default block elements are div, p and form.
  Inline elements could be used to wrap some text or hyperlink inside a paragraph. Common default inline elements are span and a.

- Float property : Specify whether element should align to left or right. If element is positioned absolutely, float property is ignored.
 
- Overflow : Work for block elements with specific height, and it specify what happens if content of element overflows the size of element (visible, hidden, scroll)

- Clear : Specifies on which side of an element floating elements are not allowed to float.

Margins of two or more elements(which may be next to one another or nested) overlap and form a single margin. The resulting margin width is the maximum of two margin widths so one **margin colapsed**. Margins of floating and absolutely
positioned elements never collapse, so one of the solution is to avoid this probelem is : 

```html
float:left
clear:both
```

CSS calc() function
-------------------

When working with fixed height or width of element, adding padding will extend element size, so one quick fix is to use **calc() function**
 and subtract size of padding added. Mind the spaces before and after operator.

```html
height:calc(100px - 2em)
```

Size of viewport (misc. Wrapper element in HTML markup)
----------------------------------------------------------------

Best practice to center main part of the website (for example menu and content) is to use wrapper element, and to assign heigth to this element. Then use can use relative measures on child element that are
 nested in wrapper element. In CSS3 there are new units: Viewportwidth(vw) and Viewportheight(vh). With them we can size elements to be relative to size of viewport or resolution of your screen (1vw = 1% of size of viewport),
 so if you want to set element to full width of the screen you can set element width to 100vw.

```html
    #wrapper {
        height:100vh;
    }
    #header {
        padding:0.5em;
        background-color: lightgreen;
        height:3em;
    }
    #content {
        padding:0.5em;
        background-color: lightskyblue;
        height:calc(100% - 6em - 3em);
        overflow-y: auto;
    }
    #footer {
        padding:0.5em;
        background-color: lightsalmon;
        height:3em;
    }
```     