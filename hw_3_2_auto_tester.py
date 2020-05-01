import sys
import itertools
import re

if len(sys.argv) < 2:
  print("Missing regexp as first parameter.")
  sys.exit()

if len(sys.argv) < 3:
  print("Missing maximum length as second parameter.")
  sys.exit()


input = sys.argv[1]
max_length = int(sys.argv[2])

print()
print("HW-3-2 Automatic Tester")
print("https://github.com/nemkin/scripts/blob/master/hw_3_2_auto_tester.py")
print()

regexp = '^' + input.replace('+','|').replace('e','').replace('u','|') + '$'
print()
print("Original regexp: {}".format(input))
print("Translated regexp in Python format: {}".format(regexp))
print()
print("Checking on input strings with a maximum length of {}...".format(max_length))

def generate_tests(length):
    chars = "01"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

number_of_tests = 0
example_count = 20

false_negatives = 0
false_positives = 0

false_negative_examples = []
false_positive_examples = []

for i in range(max_length+1):
    for test in generate_tests(i):
        number_of_tests += 1

        should_match = "00" not in test
        does_match = re.search(regexp, test) is not None
  
        if test == "":
          test = "empty string"
        if should_match != does_match:
          if should_match and not does_match:
            false_negatives += 1
            if len(false_negative_examples) < example_count:
              false_negative_examples.append(test)
          if not should_match and does_match:
            false_positives += 1
            if len(false_positive_examples) < example_count:
              false_positive_examples.append(test)

print("Number of testcases: {}".format(number_of_tests))
print("Maximum length of testcases: {}".format(max_length))
print()
print("False positives: {}".format(false_positives))
print("Examples of false positives: " + ", ".join(false_positive_examples))
print()
print("False negatives: {}".format(false_negatives))
print("Examples of false negatives: " + ", ".join(false_negative_examples))

if false_positives + false_negatives == 0:
  print("Verdict: \033[1;32;40mPossibly CORRECT, check manually.")
else:
  print("Verdict: \033[1;31;40mINCORRECT")

