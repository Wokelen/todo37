from django.db import models
from core.models import User
from todolist.models import BaseModel


class Board(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=255)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    def __str__(self):
        return self.title


class BoardParticipant(BaseModel):
    class Meta:
        unique_together = ("board", "user")

    class Role(models.IntegerChoices):
        owner = 1, "Владелец"
        writer = 2, "Редактор"
        reader = 3, "Читатель"

    board = models.ForeignKey(
        Board,
        verbose_name="Доска",
        on_delete=models.PROTECT,
        related_name="participants",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.PROTECT,
        related_name="participants",
    )
    role = models.PositiveSmallIntegerField(
        verbose_name="Роль", choices=Role.choices, default=Role.owner
    )
    editable_roles: list[tuple[int, str]] = Role.choices[1:]


class GoalCategory(BaseModel):

    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)
    board = models.ForeignKey(Board,  on_delete=models.PROTECT, related_name="categories")

    def __str__(self):
        return self.title


class Goal(BaseModel):
    class Status(models.IntegerChoices):
        to_do = 1, "К выполнению"
        in_progress = 2, "В процессе"
        done = 3, "Выполнено"
        archived = 4, "Архив"

    class Priority(models.IntegerChoices):
        low = 1, "Низкий"
        medium = 2, "Средний"
        high = 3, "Высокий"
        critical = 4, "Критический"

    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(to=GoalCategory, on_delete=models.PROTECT)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.to_do)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, default=Priority.medium)

    def __str__(self):
        return self.title


class GoalComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
