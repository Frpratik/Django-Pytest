import pytest
from django.urls import reverse
from myapp.models import Blog

@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "Welcome to Pytest Showcase" in response.content.decode()

@pytest.mark.django_db
def test_blog_list_view(client):
    Blog.objects.create(title="Blog 1", content="Content for Blog 1")
    response = client.get(reverse("blog_list"))
    assert response.status_code == 200
    assert "Blog 1" in response.content.decode()
