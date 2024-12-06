from myapp.forms import BlogForm

def test_blog_form_valid():
    form = BlogForm(data={"title": "Test Blog", "content": "Test Content"})
    assert form.is_valid()

def test_blog_form_invalid():
    form = BlogForm(data={"title": "", "content": "Test Content"})
    assert not form.is_valid()
    assert "title" in form.errors
