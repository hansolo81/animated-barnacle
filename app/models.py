from django.db import models


class Tribe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name
