from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment

posts = [
        {
          'title': 'التدوينة الاولى',
          'content': 'نص التدوينة الاولى كنص تجريبي',
          'post_date': '17-11-2022',
          'author': 'والزين نبيل'
        }, {
          'title': 'التدوينة الثانية',
          'content': 'نص التدوينة الثانية كنص تجريبي',
          'post_date': '19-11-2022',
          'author': 'والزين حادة'
        },  {
          'title': 'التدوينة الثالثة',
          'content': 'نص التدوينة الثالثة كنص تجريبي',
          'post_date': '27-11-2022',
          'author': 'والزين نبيل'
        },{
          'title': 'التدوينة الرابعة',
          'content': 'نص التدوينة الرابعة كنص تجريبي',
          'post_date': '10-12-2022',
          'author': 'بنحسين محمد'
        },
    ]

def home(request):
  
    context = {
            'title': 'الصفحة الرئيسية',
            'posts': Post.objects.all(),
            }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form = NewComment()
    new_comment = None

    context = {
      'title': post,
      'post': post,
      'comments': comments,
      'comment_form': comment_form,
    }

    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()

    return render(request, 'blog/detail.html', context)
