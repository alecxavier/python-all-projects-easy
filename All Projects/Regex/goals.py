import re

goals = """
June 11, 2021 - June 20, 2021
- Math: 
- Review and Practice
- Relearn everything that has to do with Fractions.
- Solving equations & inequalities.
- Analyzing the number of solutions to linear equations.
- Linear equations with unknown coefficients.
- Multi-step inequalities.
- Compound inequalities.
- Working with units.
- Rate conversion.
- Appropriate units.
- Word problems with multiple units.
- Linear equations & graphs.
- Two-variable linear equations intro.
- Slope.
- Horizontal & vertical lines.
- x-intercepts and y-intercepts.
- Applying intercepts and slope.
- Forms of linear equations.
- Intro to slope-intercept form.
- Graphing slope-intercept equations.
- Writing slope-intercept equations.
- Point-slope form.
- Standard form.
- Summary: Forms of two-variable linear equations.
- Systems of equations.
- Introduction to systems of equations.
- Solving systems of equations with substitution.
- Solving systems of equations with elimination.
- Equivalent systems of equations.
- A number of solutions to systems of equations.
- Systems of equations word problems.
- Economics:
- Unit: Forms of Competition.
- Unit: Market Failure and the Role of Government.
- Learn the Economics and Basic Geography of 10 Most Powerful Economies:
- China
- United States
- India
- Japan
- Germany
- Russia
- France
- Indonesia
- United Kingdom
- Brazil
- Learn about Property Rights.
- Know all the states in the USA.
- Know all the cities in China.
- Learn about Democracy and Republicanism.
- Programming: 
- Functions and Nested Functions.
- Combine what you have learned in Data-structures with Functions and Nested Functions.
- Learn OOP.
- Learn File Objects.
- Learn the following python modules:
- file input/output
- regex
- random
- range
- syntax
- date&time module
- Reading:
- Finish 'Why Nations Fail" book by 250/464
"""

a = re.compile(r"\w")
matching = a.finditer(goals)

for matches in matching:
    print(matches)

