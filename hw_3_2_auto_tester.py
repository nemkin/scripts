import sys
import itertools
import re

class bash:
    green = '\033[92m'
    red = '\033[91m'
    end_color = '\033[0m'
    clean_line = '\033[K'

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

regexp = '^(' + input.replace('+','|').replace('e','').replace('u','|') + ')$'
print("Original regexp: {}".format(input))
print("Translated regexp in Python format: {}".format(regexp))
print()

def generate_tests(length):
    chars = "01"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

number_of_tests = 0
example_count = 20

true_negatives = 0
true_positives = 0
false_negatives = 0
false_positives = 0

false_negative_examples = []
false_positive_examples = []

for i in range(max_length+1):
    for test in generate_tests(i):

        number_of_tests += 1
        print("Checking on input strings with a maximum length of {}... Length: {}, Test case: {}".format(max_length, i, number_of_tests), end = '\r')

        should_match = "00" not in test
        does_match = re.search(regexp, test) is not None
  
        if test == "":
          test = "empty string"
        
        if should_match == does_match:
          if should_match and does_match:
            true_positives += 1
          if not should_match and not does_match:
            true_negatives += 1
        else:
          if should_match and not does_match:
            false_negatives += 1
            if len(false_negative_examples) < example_count:
              false_negative_examples.append(test)
          if not should_match and does_match:
            false_positives += 1
            if len(false_positive_examples) < example_count:
              false_positive_examples.append(test)

sys.stdout.write(bash.clean_line)
print("Checking on input strings with a maximum length of {}... Done.".format(max_length))
print("Number of testcases: {}".format(number_of_tests))
print()
print("True positives: {}".format(true_positives))
print("True negatives: {}".format(true_negatives))
print("False positives: {}".format(false_positives))
print("False negatives: {}".format(false_negatives))
print()
print("Examples of false positives: " + ", ".join(false_positive_examples))
print("Examples of false negatives: " + ", ".join(false_negative_examples))
print()
print("Precision: {:.4f}%".format(true_positives / (true_positives + false_positives) * 100))
print("Recall: {:.4f}%".format(true_positives / (true_positives + false_negatives) * 100))
print()
if false_positives + false_negatives == 0:
  print("Verdict: {}Possibly CORRECT, check manually.{}".format(bash.green, bash.end_color))
else:
  print("Verdict: {}INCORRECT{}".format(bash.red, bash.end_color))
