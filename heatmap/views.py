from django.shortcuts import render


def index(request):
    """Render the index page."""

    return render(request, "heatmap/index.html")