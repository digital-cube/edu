import sys

'''
K1,KX,K2  (pobedio domacin, nereseno, pobedio gost)
P1,PX,P2  (na poluvremenu pobedio domacin, nereseno, ... gost)

1-X,1-1,1-2,
X-1,X-X,X-2,
2-1,2-X,2-2

0-1,0-2,3+   (ukupan broj golova na utakmic)

F1:F2 (H1:H2)
'''


def parse_result(res_str):

    res_str = res_str.replace(' ', '')

    ftht = res_str.split('(')
    if len(ftht) != 2:
        return False, 'INVALID_ARGUMENTS'

    if ftht[1][-1] != ')':
        return False, 'INVALID_ARGUMENTS'

    ftht[1] = ftht[1][:-1]

    ft = ftht[0].split(':')

    if len(ft) != 2:
        return False, 'INVALID_ARGUMENTS'

    ht = ftht[1].split(':')

    if len(ht) != 2:
        return False, 'INVALID_ARGUMENTS'

    try:
        f1 = int(ft[0])
        f2 = int(ft[1])
        h1 = int(ht[0])
        h2 = int(ht[1])
    except ValueError:
        return False, 'INVALID_ARGUMENTS'

    if f1 < 0 or f2 < 0 or h1 < 0 or h2 < 0:
        return False, 'INVALID_ARGUMENTS'

    if f1 < h1 or f2 < h2:
        return False, 'INVALID_ARGUMENTS'

    return True, {'F1': f1, 'F2': f2, 'H1': h1, 'H2': h2}


def stop(msg):
    print(msg)
    sys.exit()

def assert_test(value, msg):

    if value:
        return

    stop("! FAILED {}".format(msg))


def test_parse_invalid_argument_type_1():

    result = parse_result("1:01:0)")

    assert_test(not result[0], "test_parse_invalid_argument_type_1 (1)")
    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_type_1 (2)")

    print('PASSED test_parse_invalid_argument_type_1')


def test_parse_invalid_argument_type_2():

    result = parse_result("1:0 1:0")

    assert_test(not result[0], "test_parse_invalid_argument_type_2 (1)")
    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_type_2 (2)")

    print('PASSED test_parse_invalid_argument_type_2')


def test_parse_invalid_argument_type_3_missing_closing_parenthesis():

    result = parse_result("1:0 (1:2")

    assert_test(not result[0], "test_parse_invalid_argument_type_3_missing_closing_parenthesis (1)")

    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_type_3_missing_closing_parenthesis (2)")


    print('PASSED test_parse_invalid_argument_type_3_missing_closing_parenthesis')


def test_parse_invalid_argument_invalid_final_time_format():

    result = parse_result("0;1 (0:1)")

    assert_test(not result[0], "test_parse_invalid_argument_invalid_final_time_format (1)")

    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_invalid_final_time_format (2)")

    print('PASSED test_parse_invalid_argument_invalid_final_time_format')

def test_parse_invalid_argument_invalid_half_time_format():

    result = parse_result("0:1 (0;2)")

    assert_test(not result[0], "test_parse_invalid_argument_invalid_half_time_format (1)")

    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_invalid_half_time_format (2)")

    print('PASSED test_parse_invalid_argument_invalid_half_time_format')


def test_parse_invalid_argument_invalid_type_not_number():

    result = parse_result("0:1 (0:X)")

    assert_test(not result[0], "test_parse_invalid_argument_invalid_type_not_number (1)")

    assert_test(result[1] == 'INVALID_ARGUMENTS', "test_parse_invalid_argument_invalid_type_not_number (2)")

    print('PASSED test_parse_invalid_argument_invalid_type_not_number')


def test_parse_0_1_0_1():
    result = parse_result("0:1 (0:1)")

    assert_test(result[0], "test_parse_0_1_0_1 (1)")
    assert_test(result[1] == {'F1': 0, 'F2': 1, 'H1': 0, 'H2': 1}, "test_parse_0_1_0_1")
    print('PASSED test_parse_0_1_0_1')

def test_parse_0_1_1_1():
    result = parse_result("0:1 (1:1)")

    assert_test(not result[0], "test_parse_0_1_1_1 (1)")
    print('PASSED test_parse_0_1_1_1')


def test_parse_0_1_minus1_1():
    result = parse_result("0:1 (-1:1)")

    assert_test(not result[0], "test_parse_0_1_minus1_1 (1)")
    print('PASSED test_parse_0_1_minus1_1')

def test_parse_0_111_0_1():
    result = parse_result("0:111 (0:1)")

    assert_test(result[0], "test_parse_0_111_0_1 (1)")
    assert_test(result[1] == {'F1': 0, 'F2': 111, 'H1': 0, 'H2': 1}, "test_parse_0_111_0_1")
    print('PASSED test_parse_0_111_0_1')


def test_parse_invalid_argument_type_pera_zika_laza():

    assert_test(not parse_result('pera zika laza')[0], "test_parse_invalid_argument_type_pera_zika_laza")

def run_tests():

    test_parse_invalid_argument_type_1()
    test_parse_invalid_argument_type_2()
    test_parse_invalid_argument_type_3_missing_closing_parenthesis()
    test_parse_invalid_argument_invalid_final_time_format()
    test_parse_invalid_argument_invalid_half_time_format()
    test_parse_invalid_argument_invalid_type_not_number()
    test_parse_0_1_0_1()
    test_parse_0_1_1_1()
    test_parse_0_1_minus1_1()
    test_parse_0_111_0_1()
    test_parse_invalid_argument_type_pera_zika_laza()


if __name__=="__main__":
    run_tests()

