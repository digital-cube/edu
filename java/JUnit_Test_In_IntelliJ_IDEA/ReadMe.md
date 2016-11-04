# JUnit test in IntelliJ IDEA (JAVA)

The topics discussed were:
  - About JUnit tests
  - Opening “Tests” directory in current project (IntelliJ IDEA)
  - Creating test class
  - Creating unit test for current method
  - Executing of test
  - Unit test running life-cycle
  - Annotate a method with @Ignor
  - setUp and tearDown methods
  - Timeout test
  - Timeout Rule (applies to all test cases in the test class)
  - Run test with Coverage
  
### About JUnit tests

Unit testing is the process of examining a small unit, or piece, of software to verify that it meets the business rules provided. The goal is to assert the expected behavior or state. It is important to understand that JUnit is not part of the standard Java class library. But it does come included with some of the popular IDEs. 

Good unit testing is critical to the success of your application. Have you ever had a game where you were playing crash right as you were getting ready to battle the bad guy? Or when visiting a website, you receive a HTTP 404 Message Page Not Found. These types of problems cause the end user to lose confidence in your application. So you want to make sure that your thoroughly test every possible scenario. This can be time consuming, but using JUnit, you can run several tests with one execution.

When testing, we need to identify any inputs to methods in our code as well as expected results. It is important to note that once all unit testing is complete, you still need to run integration tests for any applications that have complex user interfaces or other component interaction. An integration test aims to test the behavior of a component or the integration between multiple components. These tests are used to test the entire system.

Finally, another type of testing is performance testing. These tests are used to benchmark the software by running repeatedly to simulate user traffic on your application. The purpose is to ensure the code runs fast enough under a high traffic load. JUnit not set up to do integration or performance testing, but it will help you get your unit testing done completely and efficiently.

JUnit is used primarily to do basic unit tests. One of the benefits of JUnit is that the tests are done so that they do not require human judgment to interpret. When we create a test, we identify the expected result. Then we compare that to the actual result. If they're the same, then we know the test worked. If they're different, then we know we have an error that we need to go back and fix. Another benefit is it's easy to run many test cases at the same time.

There are several potential naming conventions for creating JUnit tests, but a widely used solution is to add the suffix test to the names of the classes being tested and create them in a new package called test. As a general rule, a test name should explain what the test does. If that is done correctly, reading the action implementation code can be avoided. When you do need to create a unit test, you can follow these simple steps:
 - Annotate a method with @Test.
 - Make sure to import org.junit.Assert.*
 - Add your assert statements to test the program logic.

### Opening "Tests" directory in current project (IntelliJ IDEA) 

To adjust the working environment for JUnit testing of your code follow these steps:
- Open ItelliJ and create new Java project
- Right click on "src" directory and create new java class with methods (for example "Karta.java")
- Right click on current project directory, then select "New", then select "Directory", and then enter new directory name (for example "tests")
- Click to "File", then select "Project Structure" (Ctrl+Alt+Shift+S)
- Select "Modules", then select "tests" directory, then select Tests flag and then OK.

![alt tag](https://github.com/digital-cube/edu/blob/master/java/JUnit_Test_In_IntelliJ_IDEA/junit01.PNG)

### Creating test class

To create test class for existing class in current project follow these steps:
- Put cursor on class name and then press Alt+Enter, then select "Create Test"
- In new opened window select JUnit4 as testing library and then click Fix button if exist
- Select method which you want to test and press OK.

There are several potential naming conventions for creating JUnit tests, but a widely used solution is to add the suffix test to the names of the classes being tested and create them in a new package called test.

In this case IntelliJ will create new test class, for testing current class, in "tests" directory (for example "KartaTest").

### Creating unit test for current method
As a general rule, a test name should explain what the test does. If that is done correctly, reading the action implementation code can be avoided. 
When you do need to create a unit test, for some method, you can follow these simple steps:
 - Annotate a method with @Test
 - Make sure to import org.junit.Assert.*
 - Add your assert statements to test the program logic (An example might be the assert equals, which takes two values, the expected value and the result of testing the program class)

### Executing of test
If you want to execut all tests contetned in the test class, put cursor on name of test class and then press Ctrl+Shift+F10.
If you want to execut just one specific test method, put cursor on name of specific test method, inside test clas, and then press Ctrl+Shift+F10.
If you want to repeat just last test, press Shift+F10.

### Unit test running life-cycle 
When you run unit test from some test class, framework will call an instance of current test object. That object will then call the one of test method and execute the test. After that, object will be destroyed. 
Then framework will regenerate a new instanse of test object and call next method to test it.
Each of these tests is being executed on its own.

### Annotate a method with @Ignor
This is another JUnit annotation which refers to the method that will be excluded from testing. Also you can put message, inside the parentheses, and explain reason for ignoring that method from testing.
```sh
@Ignore ("Exception throwing now yet defined")
@Test (expected = IllegalStateException.class)
public void testMethod1() throws Exception {
[...]
}
```

### setUp and tearDown methods
Method setUp() runs before every test invocation. Method tearDown() runs after every test method. 

The @BeforeClass and @AfterClass annotated methods will be run exactly once during your test run - at the very beginning and end of the test as a whole, before anything else is run. In fact, they're run before the test class is even constructed, which is why they must be declared static.

The @Before and @After methods will be run before and after every test case, so will probably be run multiple times during a test run.
```sh
@BeforeClass
public static void setUpBeforeClass() throws Exception {
}
@AfterClass
public static void tearDownAfterClass() throws Exception {
}
@Before
public void setUp() throws Exception {
}
@After
public void tearDown() throws Exception {
}
```

So let's assume you had three tests in your class, the order of method calls would be:

```sh
setUpBeforeClass()
  (Test class first instance constructed and the following methods called on it)
    setUp()
    test1()
    tearDown()
  (Test class second instance constructed and the following methods called on it)
    setUp()
    test2()
    tearDown()
  (Test class third instance constructed and the following methods called on it)
    setUp()
    test3()
    tearDown()
tearDownAfterClass()
```
### Timeout test
You can optionally specify timeout in milliseconds to cause a test method to fail if it takes longer than that number of milliseconds. If the time limit is exceeded, then the failure is triggered by an Exception being thrown:
```sh
@Test(timeout=1000)
public void testWithTimeout() {
  ...
}
```
This is implemented by running the test method in a separate thread. If the test runs longer than the allotted timeout, the test will fail and JUnit will interrupt the thread running the test. If a test times out while executing an interruptible operation, the thread running the test will exit (if the test is in an infinite loop, the thread running the test will run forever, while other tests continue to execute).

### Timeout Rule (applies to all test cases in the test class)
The Timeout Rule applies the same timeout to all test methods in a class, and will currently execute in addition to any timeout specified by the timeout parameter on an individual Test annotation.:
```sh
@Rule
    public Timeout globalTimeout = Timeout.seconds(10); // 10 seconds max per method tested

```
### Run test with Coverage
Viewing code coverage helps you detect pieces of your source code that are not affected by simulation.
![alt tag](https://github.com/digital-cube/edu/blob/master/java/JUnit_Test_In_IntelliJ_IDEA/junit02.PNG)
  



