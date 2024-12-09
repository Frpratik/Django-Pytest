import pytest

@pytest.mark.django_db
def test_sample_blog_fixture(sample_blog):
    assert sample_blog.title == "Fixture Blog"
