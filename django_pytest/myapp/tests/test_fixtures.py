def test_sample_blog_fixture(sample_blog):
    assert sample_blog.title == "Fixture Blog"
    assert sample_blog.content == "This is a blog created by a fixture."
