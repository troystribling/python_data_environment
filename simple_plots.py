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

    pyplot.plot(xs, variance,     'g-',  label='variance')
    pyplot.plot(xs, bias_squared, 'r-.', label='bias^2')
    pyplot.plot(xs, total_error,  'b:',  label='total error')

    pyplot.legend(loc=9)
    pyplot.xlabel("model complexity")
    pyplot.title("The Bias-Variance Tradeoff")
    pyplot.show()

def scatter_plot():

    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    pyplot.scatter(friends, minutes)

    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        pyplot.annotate(label,
                        xy=(friend_count, minute_count),
                        xytext=(5, -5),
                        textcoords='offset points')

    pyplot.title("Daily Minutes vs. Number of Friends")
    pyplot.xlabel("# of friends")
    pyplot.ylabel("daily minutes spent on the site")
    pyplot.show()

def scatter_plot_axes(equal_axes=False):

    test_1_grades = [ 99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    pyplot.scatter(test_1_grades, test_2_grades)
    pyplot.xlabel("test 1 grade")
    pyplot.ylabel("test 2 grade")

    if equal_axes:
        pyplot.title("Axes Are Comparable")
        pyplot.axis("equal")
    else:
        pyplot.title("Axes Aren't Comparable")

    pyplot.show()

def pie_chart():
    pyplot.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])
    pyplot.axis("equal")
    pyplot.show()
