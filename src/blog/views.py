from django.shortcuts import render

# Create your views here.
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
            'title': 'الثفحة الرئيسية',
            'posts': posts,
            }
    return render(request, 'blog/index.html', context)
