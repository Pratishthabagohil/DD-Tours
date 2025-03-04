from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    number_of_persons = models.IntegerField()
    departure_date = models.DateField()
    return_date = models.DateField()
    transportation_method = models.CharField(
        max_length=10, 
        choices=[('Flight', 'Flight'), ('Train', 'Train')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} for {self.place}"

class Location(models.Model):
    line = models.TextField(null=True, blank=True)
    Cname = models.CharField(max_length=255, default="India")
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    altitude = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    includes = models.JSONField(default=list)
    about = models.TextField()
    image = models.ImageField(upload_to='location_images/')
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    backimage = models.ImageField(upload_to='location_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="itinerary")
    DDate = models.DateField()
    day = models.IntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['day']  # Ensures correct order in admin & frontend

    def __str__(self):
        return f"Day {self.day} - {self.location.name}"
