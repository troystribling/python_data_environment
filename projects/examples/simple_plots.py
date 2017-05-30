from matplotlib import pyplot
from collections import Counter

def line_plot():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    pyplot.plot( years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
    pyplot.title("Nominal GDP")
    pyplot.ylabel("Billions of $")
    pyplot.show()

def bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    xs = [i + 0.1 for i, _ in enumerate(movies)]

    pyplot.bar(xs, num_oscars)
    pyplot.ylabel("# of Academy Awards")
    pyplot.title("My Favorite Movies")
    pyplot.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

    pyplot.show()

def histogram():
    grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    pyplot.bar([x - 4 for x in histogram.keys()],  histogram.values(),  8)
    pyplot.axis([-5, 105, 0, 5])

    pyplot.xticks([10 * i for i in range(11)])
    pyplot.xlabel("Decile")
    pyplot.ylabel("# of Students")
    pyplot.title("Distribution of Exam 1 Grades")
    pyplot.show()


def multiple_line_charts():

    variance     = [1,2,4,8,16,32,64,128,256]
    bias_squared = [256,128,64,32,16,8,4,2,1]
    total_error  = [x + y for x, y in zip(variance, bias_squared)]

    xs = range(len(variance))

    pyplot.plot(xs, variance,     'g-',  label='variance')    # green solid line
    pyplot.plot(xs, bias_squared, 'r-.', label='bias^2')      # red dot-dashed line
    pyplot.plot(xs, total_error,  'b:',  label='total error') # blue dotted line

    pyplot.legend(loc=9)
    pyplot.xlabel("model complexity")
    pyplot.title("The Bias-Variance Tradeoff")
    pyplot.show()
