from bisect import bisect_left
import numpy as np
import CTFd.utils.user as user

def time_to_seconds(time: str) -> int:
    HMS = time.split(":")
    return int(HMS[0]) * 3600 + int(HMS[1]) * 60 + int(HMS[2])


def scoreCross(user: user, performance_seconds: int) -> int:
    y_values = [0, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                1000, 1050, 1100]
    y_values.reverse()
    if user.gender == "F":
        x_values = [1800, 1509, 1446, 1369, 1295, 1225, 1158, 1094, 1033, 975, 920, 869, 821, 776, 734, 696, 660, 628,
                    599, 573, 550, 530, 514, 501]
    else:
        x_values = [3599, 3222, 3084, 2918, 2758, 2605, 2460, 2320, 2188, 2064, 1945, 1834, 1730, 1632, 1542, 1458, 1381, 1311, 1248, 1191, 1142, 1100, 1064, 1035]
    x_values.reverse()
    index = bisect_left(x_values, performance_seconds)
    return round(np.interp(performance_seconds, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))

def scoreRelais(performance_seconds: int) -> int:
    y_values = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                1000, 1050, 1100]
    x_values = [45000, 20702, 19696, 18557, 17555, 16556, 15695, 14837, 13980, 13127, 12410, 11697, 11120, 10547, 9977, 9408, 8977, 8549, 8123, 7835, 7549, 7266, 7121]
    y_values.reverse()
    x_values.reverse()
    index = bisect_left(x_values, performance_seconds)
    return round(np.interp(performance_seconds, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))


def scoreLongueur(performance_meters: float) -> int:
    y_values = [0, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                1000, 1050, 1100]
    x_values = [0.00, 2.02, 2.13, 2.27, 2.43, 2.59, 2.78, 2.97, 3.18, 3.40, 3.64, 3.89, 4.16, 4.45, 4.74, 5.06, 5.38,
                5.71, 6.03, 6.36, 6.67, 6.97, 7.24, 7.47]
    index = bisect_left(x_values, performance_meters)
    return round(np.interp(performance_meters, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))

def scorePoids(performance_meters: float) -> int:
    y_values = [0, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                1000, 1050, 1100]
    x_values = [0, 2.34, 2.61, 2.98, 3.37, 3.79, 4.24, 4.72, 5.24, 5.8, 6.4, 7.03, 7.7, 8.42, 9.16, 9.94, 10.74, 11.56,
                12.39, 13.2, 13.99, 14.72, 15.39, 15.96]
    index = bisect_left(x_values, performance_meters)
    return round(np.interp(performance_meters, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))

def scoreHalteres(performance_kilo: float) -> int:
    y_values = [0, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                1000, 1050, 1100]
    x_values = [0.00, 0.34, 0.36, 0.40, 0.44, 0.48, 0.52, 0.57, 0.62, 0.68, 0.74, 0.80, 0.87, 0.94, 1.01, 1.09, 1.17,
                1.25, 1.34, 1.42, 1.49, 1.57, 1.63, 1.69]
    index = bisect_left(x_values, performance_kilo)
    return round(np.interp(performance_kilo, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))



def scoreBalPet(performance_points: int) -> int:
    y_values = [0, 50, 100, 150, 200, 250, 400, 700, 950, 1000, 1050, 1100]
    x_values = [0, 1, 2, 3, 4, 5, 10, 20, 27, 28, 29, 30]
    index = bisect_left(x_values, performance_points)
    return round(np.interp(performance_points, [x_values[index-1], x_values[index]], [y_values[index-1], y_values[index]]))


def scoreRameur(user: user, performance_seconds: int) -> int:
    maxPerformance_seconds = 185
    if user.gender == "F":
        maxTime += 10
    return min(1100, max(0, maxPerformance_seconds - performance_seconds)*10)

def scoreObstacles(performance_seconds: int) -> int:
    maxPerformance_seconds = 5100
    return min(2200, max(0, maxPerformance_seconds - performance_seconds)*40)


def scoreFlechette(performance_points: int) -> int:
    return performance_points
def scoreCO(performance_points: int) -> int:
    return performance_points


