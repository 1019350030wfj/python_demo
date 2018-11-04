# -*- coding:utf-8 -*-
import re
from verbalexpressions import VerEx

# Create an example of how to test for correctly formed URLs

verbal_expression = VerEx()
# word = (verbal_expression.start_of_line('#').anything_but("#").end_of_line("#"))
# print(word.source())

verbal_expression = VerEx()
tester = (verbal_expression.
          start_of_line().
          find('http').
          maybe('s').
          find('://').
          maybe('www.').
          anything_but(' ').
          end_of_line()
          )

# Create an example URL
# test_url = "https://www.google.com"

# Test if the URL is valid
# if tester.match(test_url):
#     print("Valid URL")

# Print the generated regex
print(tester.source())  # => ^(http)(s)?(\:\/\/)(www\.)?([^\ ]*)$

# pattern = "^(http)(s)?(://)(www\.)?([^\ ]*)$"
# url = "https://www.meitu.com"
# print(re.match(pattern, url).string)
#
# verbal_expression = VerEx()
# jq = "#hello world#"
# jq_tester = (
#     verbal_expression.find('#')
#         .anything()
#         .find('#')
# )
# print(jq_tester.source())
