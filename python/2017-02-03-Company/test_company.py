from unittest import TestCase

import company


class TestVolunteer(TestCase):

    def test_001_constructor_01(self):

        with self.assertRaises(company.InvalidGenderException):
            p = company.Volunteer("pera@digitalcube.rs", "Pera", "Peric", "X")
        with self.assertRaises(company.NameShouldContainMinimum2Characters):
            p = company.Volunteer("pera@digitalcube.rs", "X", "Peric", "M")
        with self.assertRaises(company.NameShouldContainMinimum2Characters):
            p = company.Volunteer("pera@digitalcube.rs", "Pera", "X", "F")

        pera = company.Volunteer("pera@digitalcube.rs", "Pera", "Peric", "M")
        self.assertEqual('<Volunteer email="pera@digitalcube.rs", fist_name="Pera", last_name="Peric", gender="M" />', str(pera))


# class TestEmployee(TestCase):
#
#     def test_001_constructor_01(self):
#
#         pera = company.Employee("Pera", "Peric", "M", 140)
#         self.assertEqual('<Employee fist_name="Pera", last_name="Peric", gender="M" />', str(pera))


class TestCEO(TestCase):

    def test_001_constructor_01(self):

        pera = company.CEO("pera@digitalcube.rs", "Pera", "Peric", "M", 140)
        self.assertEqual('<CEO email="pera@digitalcube.rs", fist_name="Pera", last_name="Peric", gender="M" />', str(pera))


class TestDeveloperJunior(TestCase):

    def test_001_constructor_01(self):

        pera = company.DeveloperJunior("pera@digitalcube.rs", "Pera", "Peric", "M", 140)
        self.assertEqual('<DeveloperJunior email="pera@digitalcube.rs", fist_name="Pera", last_name="Peric", gender="M" />', str(pera))


class TestDeveloperSenior(TestCase):

    def test_001_constructor_01(self):

        pera = company.DeveloperSenior("pera@digitalcube.rs", "Pera", "Peric", "M", 140)
        self.assertEqual('<DeveloperSenior email="pera@digitalcube.rs", fist_name="Pera", last_name="Peric", gender="M" />', str(pera))


class TestCompany(TestCase):

    def setUp(self):

        self.digital_cube = company.Company("DigitalCUBE", "Otona Zupancica 24, Beograd")

    def test_001_constructor_01(self):

        self.assertEqual('<Company name="DigitalCUBE", address="Otona Zupancica 24, Beograd" />',
                         str(self.digital_cube))

    def test_002_add_employee_01(self):


        with self.assertRaises(company.InvalidDataTypeForNumberOfWorkHours):
            company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", {"hours": "pera"} )

        slobodan = company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", 140)
        self.digital_cube.add_employee(slobodan)
        self.assertEqual(len(self.digital_cube), 1)

    def test_003_add_employee_01(self):

        slobodan = company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", 140)
        self.digital_cube.add_employee(slobodan)
        ivo = company.DeveloperJunior("ivo@digitalcube.rs", "Ivo", "Kovacevic", "M", 140)
        self.digital_cube.add_employee(ivo)
        self.assertEqual(len(self.digital_cube), 2)

        self.assertEqual(
'''<Company name="DigitalCUBE", address="Otona Zupancica 24, Beograd">
  <DeveloperSenior email="slobodan@digitalcube.rs", fist_name="Slobodan", last_name="Dolinic", gender="M" />
  <DeveloperJunior email="ivo@digitalcube.rs", fist_name="Ivo", last_name="Kovacevic", gender="M" />
</Company>''', str(self.digital_cube))


    def test_004_add_employee_01(self):
        self.digital_cube.add_employee(company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", 140))
        with self.assertRaises(company.EmployeeMustBeUniqueInCompany):
           self.digital_cube.add_employee(company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", 140))

    def test_005_add_employee_01(self):
        self.digital_cube.add_employee(company.DeveloperSenior("slobodan@digitalcube.rs", "Slobodan", "Dolinic", "M", 140))
        self.digital_cube.add_employee(company.DeveloperJunior("ivo@digitalcube.rs", "Ivo", "Kovacevic", "M", 140))
        self.assertEqual(self.digital_cube.nr_of_workhours(), 280)
        self.digital_cube.add_employee(company.DeveloperJunior("mladen@digitalcube.rs", "Mladen", "Milicevic", "M", 140))
        self.assertEqual(self.digital_cube.nr_of_workhours(), 420)
        self.digital_cube.add_employee(company.Hygienist("gaga@digitalcube.rs", "Dragana", "Dragana", "F", 10))
        self.assertEqual(self.digital_cube.nr_of_workhours(), 420+10)

        with self.assertRaises(company.EmailNotPresentedInCompany):
            self.digital_cube.set_hierarchy("igor@digitalcube.rs", "ivo@digitalcube.rs")


        self.digital_cube.set_hierarchy("slobodan@digitalcube.rs", "ivo@digitalcube.rs")
        self.digital_cube.set_hierarchy("slobodan@digitalcube.rs", "mladen@digitalcube.rs")
        self.digital_cube.set_hierarchy("gaga@digitalcube.rs", "slobodan@digitalcube.rs")

        with self.assertRaises(company.DuplicatedMasterException):
            self.digital_cube.set_hierarchy("slobodan@digitalcube.rs", "ivo@digitalcube.rs")

        self.digital_cube.show_hierarchy()