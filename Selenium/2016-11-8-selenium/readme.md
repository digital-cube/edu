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

1. **assert** - if assertion fails, test is aborted and marked as failed : assertTitle(pattern) will fail if the title of the page doesn'T correspond to the pattern argument

2. **verify** - if a verification fails, the test doesn’t stop but a trace will be printed in the log

3. **waitFor** - these commands pause the test until a condition is satisfied or a
timeout is reached


##Types of locators##

By:
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
