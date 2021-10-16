class TvShow:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    def give_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.name} - {self.year} - {self.likes}'


class Movie(TvShow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.year} - {self.duration} - {self.likes}'


class Serie(TvShow):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'{self.name} - {self.year} - {self.season} - {self.likes}'


class PlayList():
    def __init__(self, name, list):
        self.name = name
        self._list = list

    def __getitem__(self, item):
        return self._list[item]

    @property
    def __len__(self):
        return len(self._list)





