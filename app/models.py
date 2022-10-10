from django.db import models
import itertools
from django.utils.translation import gettext_lazy as _
from collections import defaultdict


class Sprint(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField('Sprint Start')
    end = models.DateField('Sprint End')
    year = models.IntegerField(default=2022)
    order = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return self.name


class Tribe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __initiatives(self):
        domains = self.domain_set.all()
        return sum((list(x.initiative_set.all()) for x in domains), [])

    def __squads(self):
        domains = self.domain_set.all()
        return sum((list(x.squad_set.all()) for x in domains), [])

    def initiatives_count(self):
        return len(self.__initiatives())

    def squad_count(self):
        return len(self.__squads())


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

    def sprints_map(self):
        sprint_map = defaultdict(list)
        for sprint in self.sprints.all().order_by('year', 'order'):
            sprint_map[sprint.year].append(sprint)
        return sprint_map.items()

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
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Initiative(models.Model):
    class InitiativeStatus(models.TextChoices):
        NOT_STARTED = '0', _('Not Started')
        DEMAND = '1', _('Demand')
        IN_DEVELOPMENT = '2', _('In Development')
        DEPLOYED = '3', _('Deployed')

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    planned_for = models.DateField('Planned For')
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    sprints = models.ManyToManyField(Sprint)
    status = models.CharField(max_length=2, choices=InitiativeStatus.choices, default=InitiativeStatus.NOT_STARTED)

    def __str__(self):
        return self.name

    def initiative_status(self):
        return self.InitiativeStatus(self.status)

    def sprints_map(self):
        sprint_map = defaultdict(list)
        for sprint in self.sprints.all().order_by('year', 'order'):
            sprint_map[sprint.year].append(sprint)
        return sprint_map.items()

    def sprint_style(self):
        duration_map = {}
        for yr, sprints in self.sprints_map():
            start = sprints[0].order
            end = sprints[-1].order + 1
            duration_map[yr] = 'grid-column: ' + str(start) + '/' + str(end) + '; background-color: #2ecaac;'
        print(duration_map)
        return duration_map


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    manday_rate = models.DecimalField('Manday Rate', decimal_places=2, max_digits=20, default=30000000.00)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
