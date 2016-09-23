LESSON 1
========

The topics disscused were:
- CSS rule priorities
- CSS reset
- CSS units (px, em, %, pt)
- Collapsing margins (misc. Display, float, overflow and clear properties).
- CSS calc() function
- Wrapper element in HTML markup

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
 
- Overflow :

- Clear : 

Margins of two or more elements(which may be next to one another or nested) overlap and form a single margin. The resulting margin width is the maximum of two margin witdhs - **Margin Colapsed**. Margins of floating and absolutely
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

Wrapper element in HTML markup
------------------------------    