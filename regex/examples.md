
<h2>Some of metacharacter examples:<h2>

<table style="font-size:10px">
    <tr>
        <td><b>Metacharacter(s)</b></td>
        <td><b>Description</b></td>
        <td><b>Example</b></td>
    </tr>
    <tr>
        <td><b>.</b></td>
        <td>Normally matches any character except a newline.
Within square brackets the dot is literal.</td>
        <td>
         <pre>
           $string1 = "Hello World\n";
if ($string1 =~ m/...../) {
  print "$string1 has length >= 5.\n";
}
<b>Output:</b>
Hello World
 has length >= 5.
        </pre>
        </td>
    </tr>
 <tr>
        <td>( )</td>
        <td>Groups a series of pattern elements to a single element.
When you match a pattern within parentheses, you can use any of $1, $2, … later to refer to the previously matched pattern.</td>
        <td>
         <pre>
$string1 = "Hello World\n";
if ($string1 =~ m/(H..).(o..)/) {
  print "We matched '$1' and '$2'.\n";
}
<b>Output:</b>
We matched 'Hel' and 'o W'.
        </pre>
        </td>
    </tr>
<tr>
        <td><b>+</b></td>
        <td>Matches the preceding pattern element one or more times.</td>
        <td>
         <pre>
$string1 = "Hello World\n";
if ($string1 =~ m/l+/) {
  print "There are one or more consecutive letter \"l\"'s in $string1.\n";
}
<b>Output:</b>
There are one or more consecutive letter "l"'s in Hello World.
        </pre>
        </td>
    </tr>
    <tr>
        <td><b>?</b></td>
        <td>Matches the preceding pattern element zero or one time.</td>
        <td>
         <pre>
$string1 = "Hello World\n";
if ($string1 =~ m/H.?e/) {
  print "There is an 'H' and a 'e' separated by ";
  print "0-1 characters (e.g., He Hue Hee).\n";
}
<b>Output:</b>
There is an 'H' and a 'e' separated by 0-1 characters (e.g., He Hue Hee).
        </pre>
        </td>
    </tr>
</table>