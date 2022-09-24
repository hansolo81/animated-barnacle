from django.db import models


class Sprint(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField('Sprint Start')
    end = models.DateField('Sprint End')

    def __str__(self):
        return self.name


class Tribe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    sprints = models.ManyToManyField(Sprint)

    def __str__(self):
        return self.name

    def initiatives_count(self):
        return len(self.initiative_set.all())

    def squad_count(self):
        return len(self.squad_set.all())

    def month_year_iter(self):
        start_month = 9
        start_year = 2022
        end_month = 1
        end_year = 2024
        ym_start = 12 * start_year + start_month - 1
        ym_end = 12 * end_year + end_month - 1
        for ym in range(ym_start, ym_end):
            y, m = divmod(ym, 12)
            # yield y, m + 1
            yield '%s/%s' % (m + 1, y)


class Squad(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    scrum_master = models.IntegerField('SM', default=0)
    business_analysts = models.IntegerField('BA', default=0)
    frontend_dev = models.IntegerField('FE', default=0)
    backend_dev = models.IntegerField('BE', default=0)
    qa_engineer = models.IntegerField('QA', default=0)

    def __str__(self):
        return self.name




class Initiative(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    planned_for = models.DateField('Planned For')
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    sprints = models.ManyToManyField(Sprint)

    def __str__(self):
        return self.name
