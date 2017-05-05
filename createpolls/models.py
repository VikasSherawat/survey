from django.db import models,IntegrityError
from django.utils import timezone
from django.contrib.auth.models import User
import random,string
# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200)
    created = models.DateTimeField('Published On',auto_now=True)
    email = models.EmailField()
    q_num = models.CharField(max_length=16, db_index=True,unique=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
            self.email = 'sakiv.sherawat@gmail.com'
            success = False
            failures = 0
            self.q_num = ''.join(
                random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
            while not success:
                try:
                    super(Question, self).save(*args, **kwargs)
                except IntegrityError:
                    failures += 1
                    if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                        raise
                    else:
                        # looks like a collision, try another random value
                        self.q_num = ''.join(
                            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                            range(16))
                else:
                    success = True

        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice