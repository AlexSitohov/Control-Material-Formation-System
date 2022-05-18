from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
import random


def main_view(request):
    return render(request, 'main/main.html')