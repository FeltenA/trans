from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Match(models.Model):
    player1 = models.ForeignKey(
        "User",
        on_delete=models.CASCADE
    )
    player2 = models.ForeignKey(
        "User",
        on_delete=models.CASCADE
    )
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    winner = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=True
    )
    tournament = models.ForeignKey(
        "Tournament",
        on_delete=models.CASCADE,
        blank=True
    )

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError('First and second player should be different.')
        if self.winner != "" and (self.winner != self.player1 or self.winner != self.player2):
            raise ValidationError('Winner should be one of the players.')

class Tournament(models.Model):
    name = models.CharField(max_length=30)
    players = models.ManyToManyField(User)
    match = models.ForeignKey(
        "Match",
        on_delete=models.CASCADE
    )