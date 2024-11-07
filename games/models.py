from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError  # Add this import
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)  # New field for availability

    def __str__(self):
        return self.title

class Loan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)  # Optional, can be null for not yet returned loans
    due_date = models.DateTimeField(default=timezone.now() + timedelta(days=14))  # Due date 14 days from now
    
    def __str__(self):
        return f"{self.game.title} loaned by {self.borrower.username}"

    # Ensure 'returned_at' is never before 'borrowed_at'
    def clean(self):
        if self.returned_at and self.returned_at < self.borrowed_at:
            raise ValidationError({'returned_at': 'Returned date cannot be before borrowed date.'})
