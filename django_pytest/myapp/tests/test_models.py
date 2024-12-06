import pytest
from myapp.models import Blog

@pytest.mark.django_db
def test_blog_creation():
    blog = Blog.objects.create(title="Test Blog", content="This is a test blog.")
    assert Blog.objects.count() == 1
    assert blog.title == "Test Blog"
