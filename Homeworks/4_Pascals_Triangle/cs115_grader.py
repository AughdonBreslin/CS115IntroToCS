"""
" Christian Bouwense
" Grading script for CS115 assignments, see the README for usage.
"""
import hw4
import test_cases

memory_refresher = (
    "\n\n################ DONT FORGET ############\n"
    "## 5 points: Name, 5 points: Pledge    ##\n"
    "## 5 points: Docstrings (per function) ##\n"
    "#########################################\n"
)


def test_answer(func, _input, expected, cmp, multi_input=False):

    try:
        # TODO: Only works for two inputs
        if multi_input:
            student_answer = func(_input[0], _input[1])
        else:
            student_answer = func(_input)
    except:
        raise RuntimeError("Oof, %s(%s) itself crashed :\\\n" % (func.__name__, _input))

    try:
        assert(cmp(student_answer, expected))
    except:
        print ("EXPECTED ANSWER: %s(%s) == %s" % (func.__name__, _input, expected))
        print ("STUDENT ANSWER:\t %s(%s) == %s" % (func.__name__, _input, student_answer))
        raise AssertionError("Yikes, their output was incorrect :(\n")


def run_all_tests():
    
    # We will sum these up as we go (variable possible points because some
    # assignments may have more or less than 100 points).
    possible_assign_points = 0
    final_assign_points = 0

    tests_ref = test_cases.Tests()
    for test in tests_ref.tests:

        print("\n----------------------------------------------------------------------")
        print("Testing %s(): %s points" % (test["func"].__name__, test["possible_points"]))
        print("----------------------------------------------------------------------\n")

        for func_test in test["tests"]:
            try:

                # Check if we have "inputs" or "input". 
                # If it's "inputs", then use the different inputs 
                # If it's not, interpret input exactly as-is
                if "inputs" in func_test:
                    test_answer(test["func"], func_test["inputs"], func_test["expected"], test["cmp"], multi_input=True)
                else:
                    test_answer(test["func"], func_test["input"], func_test["expected"], test["cmp"])
                if "final_points" not in test:
                    test["final_points"] = 0
                test["final_points"] += func_test["points"]
            except (AssertionError, RuntimeError) as e:
                print (e)
        
        possible_assign_points += test["possible_points"]
        if "final_points" not in test:
            test["final_points"] = 0
        final_assign_points += test["final_points"]

        print ("%s/%s points" % (test["final_points"], test["possible_points"]))

    print ("\nRunning test cases: 16 points for test_pascal_row...")
    hw4.test_pascal_row()
    print("Success!")
    print("\nRunning test cases: 16 points for test_pascal_triangle...")
    hw4.test_pascal_triangle()
    print("Success!")

    print ("\n\n##### TESTING COMPLETE ######")
    print ("## Final Code Score: %s/%s ##" % (final_assign_points+32, possible_assign_points+32))
    print ("#############################\n")
    

if __name__ == '__main__':
    print (memory_refresher)
    run_all_tests()
