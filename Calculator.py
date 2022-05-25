class Calculator:
    coef_a = 0
    coef_b = 0

    def __init__(self, a, b):
        self.coef_a = a
        self.coef_b = b

    def find_vilka(self):
        return 1 / float(self.coef_a) + 1 / float(self.coef_b)

    def profit(self, coef, min, max=1000):
        return str("Выигрыш составит: " +
                   str((float(coef) * min) - min - max))

    def raschet_vilki(self, summa_max=1000):

        if self.coef_a < self.coef_b:
            summa_min = (float(self.coef_a) * summa_max) / float(self.coef_b)
            return \
                str('На коэффициент {}'.format(self.coef_a) +
                  ' ставим {} '.format(summa_max)), \
                str('На коэффициент {}'.format(self.coef_b) +
                  ' ставим {} '.format(summa_min)), \
                self.profit(coef=self.coef_a, min=summa_min)

        else:
            summa_min = (float(self.coef_b) * summa_max) / float(self.coef_a)
            return \
                str('На коэффициент {}'.format(self.coef_a) +
                  ' ставим {} '.format(summa_min)),\
                str('На коэффициент {}'.format(self.coef_b) +
                  ' ставим {} '.format(summa_max)),\
                self.profit(coef=self.coef_b, min=summa_min)
