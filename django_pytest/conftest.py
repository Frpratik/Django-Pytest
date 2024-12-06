import pytest
from myapp.models import Blog

@pytest.fixture
def sample_blog():
    return Blog.objects.create(title="Fixture Blog", content="This is a blog created by a fixture.")
