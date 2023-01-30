class Statystyka:
    def __init__(self, data):
        self.data = data
#średnia
    def mean(self):
        return sum(self.data) / len(self.data)
#średnia geometryczna
    def geometric_mean(self):
        product = 1
        for i in self.data:
            product *= i
        return product**(1/len(self.data))
#mediana
    def median(self):
        self.data.sort()
        if len(self.data) % 2 == 0:
            median1 = self.data[len(self.data)//2 - 1]
            median2 = self.data[len(self.data)//2]
            return (median1 + median2) / 2
        else:
            return self.data[len(self.data)//2]
#moda
    def mode(self):
        data_dict = dict()
        for i in self.data:
            if i in data_dict:
                data_dict[i] += 1
            else:
                data_dict[i] = 1
        mode = max(data_dict, key=data_dict.get)
        return mode
#odchylenie standardowe
    def standard_deviation(self):
        mean = self.mean()
        variance = 0
        for i in self.data:
            variance += (i - mean)**2
        variance = variance / len(self.data)
        return variance**0.5
#współczynnik korelacji
    def correlation(self, x, y):
        x_mean = self.mean(x)
        y_mean = self.mean(y)
        num = 0
        den1 = 0
        den2 = 0
        for i in range(len(x)):
            num += (x[i] - x_mean) * (y[i] - y_mean)
            den1 += (x[i] - x_mean)**2
            den2 += (y[i] - y_mean)**2
        return num / ((den1 * den2)**0.5)
#współczynnik regrasji
    def regression_coefficients(self, x, y):
        x_mean = self.mean(x)
        y_mean = self.mean(y)
        b1 = self.correlation(x, y) * self.standard_deviation(y) / self.standard_deviation(x)
        b0 = y_mean - b1 * x_mean
        return b0, b1
#kwartyle
    def quartiles(self):
        sorted_data = sorted(self.data)
        q2 = self.median()
        if self.n % 2 == 0:
            q1 = Statystyka(sorted_data[:self.n // 2]).median()
            q3 = Statystyka(sorted_data[self.n // 2:]).median()
        else:
            q1 = Statystyka(sorted_data[:self.n // 2]).median()
            q3 = Statystyka(sorted_data[self.n // 2 + 1:]).median()
        return q1, q2, q3
#odchylenie kwartylowe
    def quartile_deviations(self):
        sorted_data = sorted(self.data)
        q1, q2, q3 = self.quartiles()
        IQR = q3 - q1
        lower_bound = q1 - 1.5 * IQR
        upper_bound = q3 + 1.5 * IQR
        return lower_bound, upper_bound
#rozstęp między kwartylowy
    def interquartile_range(self):
        q1, q2, q3 = self.quartiles()
        return q3 - q1
if __name__ == '__main__':
    while True:
        print("Wybierz opcję:")
        print("1. Obliczenie średniej arytmetycznej")
        print("2. Obliczenie średniej geometrycznej")
        print("3. Obliczenie mediany")
        print("4. Obliczenie mody")
        print("5. Obliczenie odchylenia standardowego")
        print("6. Obliczenie współczynnika korelacji")
        print("7. Obliczenie współczynników regresji liniowej")
        print("8. Obliczenie kwartyli")
        print("9. Obliczenie kwartylowych odchyleń")
        print("10. Obliczenie rozstępu międzykwartylowego")
        print("11. Zakończenie programu")

        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Średnia arytmetyczna:", s.mean())
        elif choice == 2:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Średnia geometryczna:", s.geometric_mean())
        elif choice == 3:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Mediana:", s.median())
        elif choice == 4:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Moda:", s.mode())
        elif choice == 5:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Odchylenie standardowe:", s.standard_deviation())
        elif choice == 6:
            x = list(map(int, input("Podaj dane dla x oddzielone przecinkami: ").split(',')))
            y = list(map(int, input("Podaj dane dla y oddzielone przecinkami: ").split(',')))
            sx = Statystyka(x)
            sy = Statystyka(y)
            print("Współczynnik korelacji:", sx.correlation_coefficient(sy))
        elif choice == 7:
            x = list(map(int, input("Podaj dane dla x oddzielone przecinkami: ").split(',')))
            y = list(map(int, input("Podaj dane dla y oddzielone przecinkami: ").split(',')))
            sx = Statystyka(x)
            sy = Statystyka(y)
            print("Współczynniki regresji liniowej:", sx.linear_regression_coefficients(sy))
        elif choice == 8:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Kwartyle:", s.quartiles())
        elif choice == 9:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Kwartylowe odchylenia:", s.quartile_deviations())
        elif choice == 10:
            data = list(map(int, input("Podaj dane oddzielone przecinkami: ").split(',')))
            s = Statystyka(data)
            print("Rozstęp międzykwartylowy:", s.interquartile_range())
        elif choice == 11:
            print("Zakończenie programu")
            break
        else:
            print("Niepoprawna opcja, spróbuj ponownie")