# Inroduction to Selenium IDE


Selenium IDE (Integrated Development Environment) is an automated testing tool that is released as a Firefox plug-in.

**Benefits:** The most impressive aspect of using selenium IDE is that the user is not required to possess any prior programming knowledge. The minimum that the user needs is the little knowing with HTML, DOMS and JavaScript

**Limitation:** One thing is to note that Selenium IDE supports only Mozilla Firefox web browser. It is difficult to test Image based application. A few more loopholes make this tool inappropriate to be used for complex test scripts. This disadvantages are resolved with other tools like Selenium RC, WebDriver.

If you want to download Selenium IDE  the explanation can be found on the following link [Download Selenium IDE]
(http://www.software-testing-tutorials-automation.com/2011/10/how-to-download-and-install-selenium.html).


##Commands##


The Selenium API defines many of commands that can be categorized into the following:
- **Actions**
- **Accessors**
- **Assertions**

Actions are commands that change the state of the application like clicking links or buttons

Accessors inspect the state of the application and store values in variables

Assertions come in three ways:

1. **assert** - if assertion fails, test is aborted and marked as failed : assertTitle(pattern) will fail if the title of the page doesn't
correspond to the pattern argument

2. **verify** - if a verification fails, the test doesn’t stop but a trace will be printed in the log

3. **waitFor** - these commands pause the test until a condition is satisfied or a
timeout is reached


##Types of locators by:##

1. ID

2. Name

3. Link Text

4. CSS Selector
    * Tag and ID
    * Tag and class
    * Tag and attribute
    * Tag, class, and attribute
    * Inner text

5. DOM (Document Object Model)
    * getElementById
    * getElementsByName
    * dom:name
    * dom: index
6. Xpath

More information can be found from link given here [locators-in-selenium-ide] (http://www.guru99.com/locators-in-selenium-ide.html).

**Firebug**, helps us in inspecting HTML, CSS and JavaScript elements on a web page. For better use Selenium IDE we need to install Firebug, [Download Firebug](https://getfirebug.com/downloads).

Selenium IDE gives you the ability to export your tests to number of popular programming languages, including Java, C#,
Groovy, Perl, PHP, Python and Ruby.
You can also debuging your tests, [debuging] (http://www.ministryoftesting.com/2011/05/debugging-tests-in-selenium-ide/).










##Selenium IDE Example##

![Selenium IDE Example](https://raw.githubusercontent.com/digital-cube/edu/master/Selenium/2016-11-8-selenium/seleniumide.png)

##Command, Target, and Value##

The **Command**, **Target**, and **Value** entry fields display the currently selected command along with its parameters.

1. Command, Target, and Value
	* Command is the action that we wish to perform This field having all commands list for selenium ide.

2. Target
	* Target is used to identify webelement on the webpage.
	 There are different way to locating elements on the webpage like locating by Id, locating by Name,locating by XPath,
	  locating Hyperlinks by Link Text, locating by CSS

3. Value
	* this field is simple value, stored on that recorded webelement during recording or we can set new value for second run of the testcase.



##Log/Reference/UI-Element/Rollup Pane##

![Selenium IDE Example](https://raw.githubusercontent.com/digital-cube/edu/master/Selenium/2016-11-8-selenium/seleniumide2.png)


The bottom pane is used for four different functions–Log, Reference, UI-Element, and Rollup–depending on which tab is selected.

**LOG**

When you run your test case, error messages and information messages showing the progress are displayed in this pane automatically,
even if you do not first select the log tab. These messages are often useful for test case debugging. Notice the Clear button for clearing the Log.
Also notice the Info button is a drop-down allowing selection of different levels of information to log.



**Reference**

![Selenium IDE Example](https://raw.githubusercontent.com/digital-cube/edu/master/Selenium/2016-11-8-selenium/seleniumide1.png)

The Reference tab is the default selection whenever you are entering or modifying Selenese commands and parameters in Table mode.
In Table mode, the Reference pane will display documentation on the current command.
When entering or modifying commands, whether from Table or Source mode, it is critically important to ensure that the parameters specified in the
Target and Value fields match those specified in he parameter list in the Reference pane. The number of parameters provided must match the number
specified, the order of parameters provided must match the order specified, and the type of parameters provided must match the type specified.
If there is a mismatch in any of these three areas, the command will not run correctly.































