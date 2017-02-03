from abc import ABCMeta, abstractmethod

class InvalidGenderException(BaseException):
    pass

class NameShouldContainMinimum2Characters(BaseException):
    pass

class InvalidDataTypeForNumberOfWorkHours(BaseException):
    '''
    expected int or float
    '''
    pass

class EmployeeMustBeUniqueInCompany(BaseException):
    pass

class EmailNotPresentedInCompany(BaseException):
    pass

class DuplicatedMasterException(BaseException):
    pass

class DuplicatedSlaveException(BaseException):
    pass

class Person(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, email, first_name, last_name, gender):

        if gender not in ('M', 'F'):
            raise InvalidGenderException

        if len(first_name) < 2 or len(last_name) < 2:
            raise NameShouldContainMinimum2Characters

        #TODO: check email vailidity

        self.email = email.lower().strip()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def __str__(self):
        return '<{} email="{}", fist_name="{}", last_name="{}", gender="{}" />'.\
            format(self.__class__.__name__, self.email, self.first_name, self.last_name, self.gender)


class Volunteer(Person):

    def __init__(self, email, first_name, last_name, gender):
        super(Volunteer, self).__init__(email, first_name, last_name, gender)


class Employee(Person, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(Employee, self).__init__(email, first_name, last_name, gender)

        if not (isinstance(hours_per_month, int) or isinstance(hours_per_month, float)):
            raise InvalidDataTypeForNumberOfWorkHours

        self.hours_per_month = hours_per_month
        self.masters = set()
        self.slaves  = set()

    def get_work_hours_per_month(self):
        return self.hours_per_month

    def add_master(self, master):
        self.masters.add(master)

    def is_mastered_by(self, master):
        return master in self.masters

    def add_slave(self, slave):
        self.slaves.add(slave)

    def is_slave_to(self, slave):
        return slave in self.slaves

    def get_slaves(self):
        return self.slaves


class Contributor(Employee, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(Contributor, self).__init__(email, first_name, last_name, gender, hours_per_month)


class Hygienist(Contributor):
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(Hygienist, self).__init__(email, first_name, last_name, gender, hours_per_month)


class CEO(Employee):

    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(CEO, self).__init__(email, first_name, last_name, gender, hours_per_month)


class Developer(Employee, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(Developer, self).__init__(email, first_name, last_name, gender, hours_per_month)


class DeveloperJunior(Developer):
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(DeveloperJunior, self).__init__(email, first_name, last_name, gender, hours_per_month)
        self.coef = 0.2


class DeveloperSenior(Developer):
    def __init__(self, email, first_name, last_name, gender, hours_per_month):
        super(DeveloperSenior, self).__init__(email, first_name, last_name, gender, hours_per_month)
        self.coef = 1


class Company(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = {}
        self.ordered_emails_by_add_time = []

    def __str__(self):
        if not len(self):
            return '<{} name="{}", address="{}" />'. \
                format(self.__class__.__name__, self.name, self.address)

        repr = '<{} name="{}", address="{}">\n'.format(self.__class__.__name__, self.name, self.address)

        for employee_email in self.ordered_emails_by_add_time:
            repr += "  {}\n".format(self.employees[employee_email])

        repr += '</{}>'.format(self.__class__.__name__)
        return repr

    def add_employee(self, employee):
        if employee.email in self.employees:
            raise EmployeeMustBeUniqueInCompany

        self.employees[employee.email] = employee
        self.ordered_emails_by_add_time.append( employee.email )

    def nr_of_workhours(self):
        return sum([self.employees[employee_key].get_work_hours_per_month()
                    for employee_key in self.employees])

    def set_hierarchy(self, master_email, slave_email):

        if master_email not in self.employees or slave_email not in self.employees:
            raise EmailNotPresentedInCompany

        master = self.employees[master_email]
        slave = self.employees[slave_email]

        if slave.is_mastered_by(master):
            raise DuplicatedMasterException

        if master.is_slave_to(slave):
            raise DuplicatedSlaveException

        slave.add_master(master)
        master.add_slave(slave)

    def show_hierarchy(self):

        for employee_email in self.ordered_emails_by_add_time:
            employee = self.employees[employee_email]
            print ("{}".format(employee))
            for slave in employee.get_slaves():
                print("  {}".format(slave))

    def __len__(self):
        return len(self.employees)

